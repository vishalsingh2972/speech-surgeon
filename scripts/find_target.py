import os
import requests
from dotenv import load_dotenv


load_dotenv()


def find_target(audio_path, target_words):
    api_key = os.getenv("FISH_API_KEY")

    if not api_key:
        raise RuntimeError("FISH_API_KEY is missing from .env")

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
                os.path.basename(audio_path),
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

    words = []

    for segment in result.get("segments", []):
        words.append({
            "text": segment["text"].strip().lower(),
            "start": segment["start"],
            "end": segment["end"],
        })

    target_words = [
        word.lower()
        for word in target_words
    ]

    target_length = len(target_words)

    for i in range(len(words) - target_length + 1):
        candidate = words[i:i + target_length]

        candidate_words = [
            word["text"]
            for word in candidate
        ]

        if candidate_words == target_words:
            return {
                "start": candidate[0]["start"],
                "end": candidate[-1]["end"],
                "words": candidate_words,
            }

    raise RuntimeError("Target sentence was not found.")


if __name__ == "__main__":
    target = [
        "we",
        "launched",
        "the",
        "first",
        "version",
        "in",
        "march",
        "and",
        "more",
        "than",
        "3000",
        "people",
        "tried",
        "it",
        "during",
        "the",
        "first",
        "week",
    ]

    result = find_target(
        "samples/original.wav",
        target,
    )

    print()
    print("Target sentence found!")
    print()
    print(f"Start: {result['start']:.2f}s")
    print(f"End:   {result['end']:.2f}s")
    print()
    print("Sentence:")
    print(" ".join(result["words"]))
    print()