import subprocess
from pathlib import Path

INPUT = "samples/original.wav"
OUTPUT = "samples/target_sentence.wav"

START = 4.32
END = 10.08

Path(OUTPUT).parent.mkdir(parents=True, exist_ok=True)

command = [
    "ffmpeg",
    "-y",
    "-i", INPUT,
    "-ss", str(START),
    "-to", str(END),
    "-c:a", "pcm_s16le",
    OUTPUT,
]

print("Extracting target sentence...")
print(f"Start: {START}s")
print(f"End:   {END}s")
print(f"Duration: {END - START:.2f}s")

result = subprocess.run(command)

if result.returncode != 0:
    raise RuntimeError("FFmpeg failed to extract the sentence.")

print("\nDone.")
print(f"Created: {OUTPUT}")