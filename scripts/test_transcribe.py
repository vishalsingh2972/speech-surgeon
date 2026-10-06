import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("FISH_API_KEY")

if not api_key:
    raise RuntimeError("FISH_API_KEY is missing from .env")

audio_path = "samples/original.wav"

url = "https://api.fish.audio/v1/asr"

headers = {
    "Authorization": f"Bearer {api_key}",
    "model": "transcribe-1-pro",
}

data = {
    "ignore_timestamps": "false",
}

with open(audio_path, "rb") as audio_file:
    files = {
        "audio": (
            "original.wav",
            audio_file,
            "audio/wav",
        )
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
        files=files,
        timeout=120,
    )

response.raise_for_status()

result = response.json()

print("\n========== TRANSCRIPT ==========\n")
print(result.get("text"))

print("\n========== SEGMENTS ==========\n")

for segment in result.get("segments", []):
    print(
        f"[{segment['start']:.2f}s → {segment['end']:.2f}s] "
        f"{segment['text']}"
    )

print("\n========== SPEAKER TURNS ==========\n")

for turn in result.get("speaker_turns", []):
    print(
        f"[{turn['start']:.2f}s → {turn['end']:.2f}s] "
        f"{turn.get('speaker')}: {turn['text']}"
    )

print("\n========== RAW RESPONSE ==========\n")
print(result)