import subprocess
from pathlib import Path

from find_target import find_target


ORIGINAL_PATH = Path("samples/original.wav")
REPLACEMENT_PATH = Path("samples/replacement.wav")
OUTPUT_PATH = Path("samples/repaired.wav")


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


print("Speech Surgeon")
print("================")
print("Finding target sentence...")

target = find_target(
    str(ORIGINAL_PATH),
    TARGET_WORDS,
)

TARGET_START = target["start"]
TARGET_END = target["end"]

print(
    f"Target: {TARGET_START:.2f}s → "
    f"{TARGET_END:.2f}s"
)
print()

print("Extracting audio before target...")

run_ffmpeg([
    "-i",
    str(ORIGINAL_PATH),
    "-t",
    str(TARGET_START),
    "-c:a",
    "pcm_s16le",
    "tmp_before.wav",
])

print("Extracting audio after target...")

run_ffmpeg([
    "-i",
    str(ORIGINAL_PATH),
    "-ss",
    str(TARGET_END),
    "-c:a",
    "pcm_s16le",
    "tmp_after.wav",
])

print("Normalizing replacement...")

run_ffmpeg([
    "-i",
    str(REPLACEMENT_PATH),
    "-ar",
    "48000",
    "-ac",
    "2",
    "-c:a",
    "pcm_s16le",
    "tmp_replacement.wav",
])

print("Joining audio...")

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
    str(OUTPUT_PATH),
])

print()
print("Done.")
print(f"Created: {OUTPUT_PATH}")

for path in [
    Path("tmp_before.wav"),
    Path("tmp_replacement.wav"),
    Path("tmp_after.wav"),
    Path("concat.txt"),
]:
    if path.exists():
        path.unlink()

print("Temporary files removed.")