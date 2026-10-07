import os
import time
import uuid
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from fishaudio import FishAudio
from fishaudio.types import ReferenceAudio, TTSConfig
from fishaudio.utils import save

from backend.diff import find_changed_sentence
from backend.session import create_session, get_session
from backend.surgery import repair_audio
from backend.video import (
    extract_audio,
    replace_video_audio,
)


load_dotenv()


app = FastAPI(
    title="Speech Surgeon API",
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Speech Surgeon API is running"
    }


# --------------------------------------------------
# Transcript cleanup
# --------------------------------------------------

def clean_transcript(text):
    if not text:
        return ""

    if text.startswith("<|speaker:"):
        text = text.split("|>", 1)[1]

    return text.strip()


# --------------------------------------------------
# Fish ASR
# --------------------------------------------------

def transcribe_audio(
    audio_bytes,
    filename,
    content_type,
):
    api_key = os.getenv("FISH_API_KEY")

    if not api_key:
        raise RuntimeError(
            "FISH_API_KEY is missing from .env"
        )

    response = requests.post(
        "https://api.fish.audio/v1/asr",
        headers={
            "Authorization": f"Bearer {api_key}",
            "model": "transcribe-1-pro",
        },
        data={
            "ignore_timestamps": "false",
        },
        files={
            "audio": (
                filename,
                audio_bytes,
                content_type or "audio/wav",
            )
        },
        timeout=120,
    )

    response.raise_for_status()

    return response.json()


# --------------------------------------------------
# Transcribe endpoint
# --------------------------------------------------

@app.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...),
):
    video_bytes = await file.read()

    temp_video_path = Path(
        "tmp/uploaded_video"
    )

    temp_audio_path = Path(
        "tmp/uploaded_audio.wav"
    )

    temp_video_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temp_video_path.write_bytes(
        video_bytes
    )

    try:
        extract_audio(
            temp_video_path,
            temp_audio_path,
        )

        audio_bytes = temp_audio_path.read_bytes()

        result = transcribe_audio(
            audio_bytes,
            "uploaded_audio.wav",
            "audio/wav",
        )

        original_text = clean_transcript(
            result.get("text")
        )

        segments = result.get(
            "segments",
            [],
        )

        session_id = create_session(
            original_text=original_text,
            segments=segments,
            audio_bytes=audio_bytes,
            filename=file.filename,
            video_bytes=video_bytes,
        )

        return {
            "session_id": session_id,
            "text": original_text,
            "segments": segments,
            "speaker_turns": result.get(
                "speaker_turns",
                [],
            ),
        }

    finally:
        temp_video_path.unlink(
            missing_ok=True
        )

        temp_audio_path.unlink(
            missing_ok=True
        )


# --------------------------------------------------
# Find sentence timestamps
# --------------------------------------------------

def find_sentence_region(
    segments,
    target_sentence,
):
    target_words = [
        word.lower().strip(".,!?")
        for word in target_sentence.split()
    ]

    words = []

    for segment in segments:
        words.append({
            "text": segment["text"]
            .strip()
            .lower()
            .strip(".,!?"),
            "start": segment["start"],
            "end": segment["end"],
        })

    target_length = len(target_words)

    for i in range(
        len(words) - target_length + 1
    ):
        candidate = words[
            i:i + target_length
        ]

        candidate_words = [
            word["text"]
            for word in candidate
        ]

        if candidate_words == target_words:
            return {
                "start": candidate[0]["start"],
                "end": candidate[-1]["end"],
            }

    return None


# --------------------------------------------------
# Generate cloned replacement speech
# --------------------------------------------------

def generate_replacement(
    reference_audio,
    replacement_text,
    output_path,
):
    api_key = os.getenv("FISH_API_KEY")

    if not api_key:
        raise RuntimeError(
            "FISH_API_KEY is missing from .env"
        )

    reference_text = (
        "I built a small project called "
        "Speech Surgeon."
    )

    reference = ReferenceAudio(
        audio=reference_audio,
        text=reference_text,
    )

    client = FishAudio(
        api_key=api_key,
    )

    config = TTSConfig(
        format="wav",
    )

    audio = client.tts.convert(
        text=replacement_text,
        model="s2.1-pro",
        references=[reference],
        config=config,
    )

    save(
        audio,
        str(output_path),
    )


# --------------------------------------------------
# Sync Labs lip-sync
# --------------------------------------------------

def generate_lipsync(
    video_path,
    audio_path,
    output_path,
):
    api_key = os.getenv("SYNC_API_KEY")

    if not api_key:
        raise RuntimeError(
            "SYNC_API_KEY is missing from .env"
        )

    video_path = Path(video_path)
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    idempotency_key = (
        f"speech-surgeon-lipsync-{uuid.uuid4()}"
    )

    headers = {
        "x-api-key": api_key,
        "Idempotency-Key": idempotency_key,
    }

    print()
    print("================================")
    print(" Sync Labs Lip-Sync")
    print("================================")
    print()
    print(f"Video: {video_path}")
    print(f"Audio: {audio_path}")
    print()

    with open(video_path, "rb") as video_file, \
         open(audio_path, "rb") as audio_file:

        response = requests.post(
            "https://api.sync.so/v2/generate",
            headers=headers,
            files={
                "video": (
                    video_path.name,
                    video_file,
                    "video/mp4",
                ),
                "audio": (
                    audio_path.name,
                    audio_file,
                    "audio/wav",
                ),
            },
            data={
                "model": "lipsync-2",
                "options": (
                    '{"sync_mode":"cut_off"}'
                ),
            },
            timeout=120,
        )

    response.raise_for_status()

    job = response.json()

    job_id = job["id"]

    print(
        f"Sync Labs job created: {job_id}"
    )
    print(
        f"Initial status: {job.get('status')}"
    )
    print()

    while True:
        response = requests.get(
            f"https://api.sync.so/v2/generate/{job_id}",
            headers={
                "x-api-key": api_key,
            },
            timeout=60,
        )

        response.raise_for_status()

        result = response.json()

        status = result.get("status")

        print(
            f"Sync Labs status: {status}"
        )

        if status == "COMPLETED":
            output_url = result.get(
                "outputUrl"
            )

            if not output_url:
                raise RuntimeError(
                    "Sync Labs completed without "
                    "an output URL."
                )

            print()
            print(
                "Downloading lip-synced video..."
            )

            video_response = requests.get(
                output_url,
                timeout=120,
            )

            video_response.raise_for_status()

            output_path.write_bytes(
                video_response.content
            )

            print(
                f"Lip-synced video created: "
                f"{output_path}"
            )

            return

        if status in {
            "FAILED",
            "REJECTED",
        }:
            error = result.get(
                "error",
                "Unknown Sync Labs error.",
            )

            raise RuntimeError(
                f"Sync Labs lip-sync failed: "
                f"{error}"
            )

        time.sleep(5)


# --------------------------------------------------
# Repair endpoint
# --------------------------------------------------

@app.post("/repair")
async def repair(
    session_id: str = Form(...),
    edited_text: str = Form(...),
):
    # ----------------------------------------------
    # 1. Load session
    # ----------------------------------------------

    session = get_session(
        session_id
    )

    original_text = session[
        "original_text"
    ]

    segments = session[
        "segments"
    ]

    audio_bytes = session[
        "audio_bytes"
    ]

    # ----------------------------------------------
    # 2. Find changed sentence
    # ----------------------------------------------

    changed_sentence = find_changed_sentence(
        original_text,
        edited_text,
    )

    if changed_sentence is None:
        raise RuntimeError(
            "No changes were detected."
        )

    original_sentence = changed_sentence[
        "original"
    ]

    edited_sentence = changed_sentence[
        "edited"
    ]

    # ----------------------------------------------
    # 3. Find original sentence timestamps
    # ----------------------------------------------

    target = find_sentence_region(
        segments,
        original_sentence,
    )

    if target is None:
        raise RuntimeError(
            "Changed sentence was not found "
            "in the audio transcript."
        )

    # ----------------------------------------------
    # 4. Create temporary original audio
    # ----------------------------------------------

    with NamedTemporaryFile(
        suffix=".wav",
        delete=False,
    ) as temp:
        temp.write(audio_bytes)

        original_path = Path(
            temp.name
        )

    try:
        # ------------------------------------------
        # 5. Generate replacement speech
        # ------------------------------------------

        replacement_path = Path(
            f"outputs/replacement-{session_id}.wav"
        )

        replacement_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        generate_replacement(
            reference_audio=audio_bytes,
            replacement_text=edited_sentence,
            output_path=replacement_path,
        )

        # ------------------------------------------
        # 6. Perform audio surgery
        # ------------------------------------------

        output_path = Path(
            f"outputs/repaired-{session_id}.wav"
        )

        repair_audio(
            original_path=original_path,
            replacement_path=replacement_path,
            target_start=target["start"],
            target_end=target["end"],
            output_path=output_path,
        )

        # ------------------------------------------
        # 7. Store repaired audio in session
        # ------------------------------------------

        session[
            "repaired_audio_bytes"
        ] = output_path.read_bytes()

        session[
            "changed_region"
        ] = {
            "start": target["start"],
            "end": target["end"],
        }

        session[
            "original_sentence"
        ] = original_sentence

        session[
            "edited_sentence"
        ] = edited_sentence

        # ------------------------------------------
        # 8. Load original video
        # ------------------------------------------

        video_bytes = session.get(
            "video_bytes"
        )

        if video_bytes is None:
            raise RuntimeError(
                "Original video is missing "
                "from session."
            )

        original_video_path = Path(
            f"outputs/original-{session_id}.mp4"
        )

        repaired_video_path = Path(
            f"outputs/repaired-{session_id}.mp4"
        )

        original_video_path.write_bytes(
            video_bytes
        )

        # ------------------------------------------
        # 9. Replace video audio
        # ------------------------------------------

        replace_video_audio(
            video_path=original_video_path,
            audio_path=output_path,
            output_path=repaired_video_path,
        )

        # ------------------------------------------
        # 10. Return repaired video
        # ------------------------------------------

        return FileResponse(
            path=repaired_video_path,
            media_type="video/mp4",
            filename="repaired.mp4",
        )

    finally:
        original_path.unlink(
            missing_ok=True
        )


# --------------------------------------------------
# Lip-sync endpoint
# --------------------------------------------------

@app.post("/lipsync")
async def lipsync(
    session_id: str = Form(...),
):
    # ----------------------------------------------
    # 1. Load session
    # ----------------------------------------------

    session = get_session(
        session_id
    )

    video_bytes = session.get(
        "video_bytes"
    )

    repaired_audio_bytes = session.get(
        "repaired_audio_bytes"
    )

    if video_bytes is None:
        raise RuntimeError(
            "Original video is missing "
            "from session."
        )

    if repaired_audio_bytes is None:
        raise RuntimeError(
            "Repaired audio is missing. "
            "Run /repair first."
        )

    # ----------------------------------------------
    # 2. Save temporary input files
    # ----------------------------------------------

    original_video_path = Path(
        f"tmp/{session_id}-lipsync-input.mp4"
    )

    repaired_audio_path = Path(
        f"tmp/{session_id}-lipsync-audio.wav"
    )

    lipsynced_output_path = Path(
        f"outputs/lipsynced-{session_id}.mp4"
    )

    original_video_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    lipsynced_output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    original_video_path.write_bytes(
        video_bytes
    )

    repaired_audio_path.write_bytes(
        repaired_audio_bytes
    )

    try:
        # ------------------------------------------
        # 3. Send video + repaired audio
        #    to Sync Labs
        # ------------------------------------------

        generate_lipsync(
            video_path=original_video_path,
            audio_path=repaired_audio_path,
            output_path=lipsynced_output_path,
        )

        # ------------------------------------------
        # 4. Save result in session
        # ------------------------------------------

        session[
            "lipsynced_video_path"
        ] = str(lipsynced_output_path)

        # ------------------------------------------
        # 5. Return lip-synced video
        # ------------------------------------------

        return FileResponse(
            path=lipsynced_output_path,
            media_type="video/mp4",
            filename="lipsynced.mp4",
        )

    finally:
        original_video_path.unlink(
            missing_ok=True
        )

        repaired_audio_path.unlink(
            missing_ok=True
        )