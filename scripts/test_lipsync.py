import os
import time
import uuid
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SYNC_API_KEY")

if not api_key:
    raise RuntimeError("SYNC_API_KEY is missing from backend/.env")

video_path = Path("samples/lipsync-input.mp4")
audio_path = Path("samples/lipsync-audio.wav")
output_path = Path("samples/lipsynced-test.mp4")

if not video_path.exists():
    raise FileNotFoundError(video_path)

if not audio_path.exists():
    raise FileNotFoundError(audio_path)

headers = {
    "x-api-key": api_key,
    "Idempotency-Key": f"speech-surgeon-test-{uuid.uuid4()}",
}

print("================================")
print(" Speech Surgeon Lip-Sync Test")
print("================================")
print()
print(f"Video: {video_path}")
print(f"Audio: {audio_path}")
print()
print("Sending to Sync Labs...")
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
            "options": '{"sync_mode":"cut_off"}',
        },
        timeout=120,
    )

response.raise_for_status()

job = response.json()

job_id = job["id"]

print("Generation accepted.")
print(f"Job ID: {job_id}")
print(f"Initial status: {job.get('status')}")
print()

print("Waiting for result...")

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

    print(f"Status: {status}")

    if status == "COMPLETED":
        output_url = result.get("outputUrl")

        if not output_url:
            raise RuntimeError(
                "Generation completed but no outputUrl was returned."
            )

        print()
        print("Lip-sync completed.")
        print("Downloading result...")

        video_response = requests.get(
            output_url,
            timeout=120,
        )

        video_response.raise_for_status()

        output_path.write_bytes(video_response.content)

        print()
        print("================================")
        print(" SUCCESS")
        print("================================")
        print()
        print(f"Created: {output_path}")
        print(f"Size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")
        print()

        break

    if status in {"FAILED", "REJECTED"}:
        print()
        print("================================")
        print(" LIP-SYNC FAILED")
        print("================================")
        print()
        print(result)
        raise RuntimeError("Sync Labs lip-sync generation failed.")

    time.sleep(5)