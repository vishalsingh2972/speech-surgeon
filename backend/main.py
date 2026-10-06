import os
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, UploadFile
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
    version="0.1.0",
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
            "outputs/replacement.wav"
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
            "outputs/repaired.wav"
        )

        repair_audio(
            original_path=original_path,
            replacement_path=replacement_path,
            target_start=target["start"],
            target_end=target["end"],
            output_path=output_path,
        )

        # ------------------------------------------
        # 7. Load original video
        # ------------------------------------------

        video_bytes = session.get(
            "video_bytes"
        )

        if video_bytes is None:
            raise RuntimeError(
                "Original video is missing from session."
            )

        original_video_path = Path(
            "outputs/original.mp4"
        )

        repaired_video_path = Path(
            f"outputs/repaired-{session_id}.mp4"
        )

        original_video_path.write_bytes(
            video_bytes
        )

        # ------------------------------------------
        # 8. Replace video audio
        # ------------------------------------------

        replace_video_audio(
            video_path=original_video_path,
            audio_path=output_path,
            output_path=repaired_video_path,
        )

        # ------------------------------------------
        # 9. Return repaired video
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