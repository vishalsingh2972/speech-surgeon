import subprocess
from pathlib import Path

INPUT = "samples/original.wav"
OUTPUT = "samples/march.wav"

START = 6.16
END = 6.64

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

print("Extracting target segment...")
print(f"Start: {START}s")
print(f"End:   {END}s")
print(f"Output: {OUTPUT}")

result = subprocess.run(command)

if result.returncode != 0:
    raise RuntimeError("FFmpeg failed to extract the segment.")

print("\nDone.")
print(f"Created: {OUTPUT}")