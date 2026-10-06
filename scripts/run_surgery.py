import os
import subprocess
from pathlib import Path
from difflib import SequenceMatcher

from dotenv import load_dotenv
from fishaudio import FishAudio
from fishaudio.types import ReferenceAudio, TTSConfig
from fishaudio.utils import save

from find_target import find_target


load_dotenv()


# --------------------------------------------------
# Files
# --------------------------------------------------

ORIGINAL_AUDIO = Path("samples/original.wav")
REPLACEMENT_AUDIO = Path("samples/replacement.wav")
OUTPUT_AUDIO = Path("samples/repaired.wav")


# --------------------------------------------------
# Original and edited sentence
# --------------------------------------------------

ORIGINAL_TEXT = (
    "We launched the first version in March, "
    "and more than 3000 people tried it "
    "during the first week."
)

EDITED_TEXT = (
    "We launched the first version in June, "
    "and more than five thousand people tried it "
    "during the first week."
)


# Fish ASR words used to locate the original sentence
TARGET_WORDS = [
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


# --------------------------------------------------
# Text diff
# --------------------------------------------------

def detect_changes(original, edited):
    original_words = original.split()
    edited_words = edited.split()

    matcher = SequenceMatcher(
        None,
        original_words,
        edited_words,
    )

    changes = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():

        if tag == "equal":
            continue

        changes.append({
            "type": tag,
            "original": " ".join(original_words[i1:i2]),
            "edited": " ".join(edited_words[j1:j2]),
        })

    return changes


# --------------------------------------------------
# FFmpeg helper
# --------------------------------------------------

def run_ffmpeg(args):
    command = ["ffmpeg", "-y", *args]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("FFmpeg command failed")


# --------------------------------------------------
# Generate replacement speech
# --------------------------------------------------

def generate_replacement():

    api_key = os.getenv("FISH_API_KEY")

    if not api_key:
        raise RuntimeError(
            "FISH_API_KEY is missing from .env"
        )

    reference_text = (
        "I built a small project called Speech Surgeon."
    )

    print("Generating replacement speech...")

    with open(ORIGINAL_AUDIO, "rb") as f:
        reference_audio = f.read()

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
        text=EDITED_TEXT,
        model="s2.1-pro",
        references=[reference],
        config=config,
    )

    save(
        audio,
        str(REPLACEMENT_AUDIO),
    )

    print(
        f"Created replacement: "
        f"{REPLACEMENT_AUDIO}"
    )


# --------------------------------------------------
# Main pipeline
# --------------------------------------------------

print()
print("Speech Surgeon")
print("================")
print()

print("1. Finding target sentence...")

target = find_target(
    str(ORIGINAL_AUDIO),
    TARGET_WORDS,
)

target_start = target["start"]
target_end = target["end"]

print(
    f"Target region: "
    f"{target_start:.2f}s → {target_end:.2f}s"
)

print()

print("2. Detecting text changes...")

changes = detect_changes(
    ORIGINAL_TEXT,
    EDITED_TEXT,
)

for change in changes:
    print(
        f"- {change['original']} "
        f"→ {change['edited']}"
    )

print()

print("3. Generating replacement speech...")

generate_replacement()

print()

print("4. Extracting audio before target...")

run_ffmpeg([
    "-i",
    str(ORIGINAL_AUDIO),
    "-t",
    str(target_start),
    "-c:a",
    "pcm_s16le",
    "tmp_before.wav",
])

print("5. Extracting audio after target...")

run_ffmpeg([
    "-i",
    str(ORIGINAL_AUDIO),
    "-ss",
    str(target_end),
    "-c:a",
    "pcm_s16le",
    "tmp_after.wav",
])

print("6. Normalizing replacement audio...")

run_ffmpeg([
    "-i",
    str(REPLACEMENT_AUDIO),
    "-ar",
    "48000",
    "-ac",
    "2",
    "-c:a",
    "pcm_s16le",
    "tmp_replacement.wav",
])

print("7. Joining original + replacement + original...")

with open("concat.txt", "w", encoding="utf-8") as f:
    f.write("file 'tmp_before.wav'\n")
    f.write("file 'tmp_replacement.wav'\n")
    f.write("file 'tmp_after.wav'\n")

run_ffmpeg([
    "-f",
    "concat",
    "-safe",
    "0",
    "-i",
    "concat.txt",
    "-c:a",
    "pcm_s16le",
    str(OUTPUT_AUDIO),
])


# --------------------------------------------------
# Cleanup
# --------------------------------------------------

for path in [
    Path("tmp_before.wav"),
    Path("tmp_after.wav"),
    Path("tmp_replacement.wav"),
    Path("concat.txt"),
]:
    if path.exists():
        path.unlink()


print()
print("================================")
print("Speech Surgeon pipeline complete")
print("================================")
print()
print(f"Original: {ORIGINAL_AUDIO}")
print(f"Repaired: {OUTPUT_AUDIO}")
print()