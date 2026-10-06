import os
from pathlib import Path
from fishaudio.types import ReferenceAudio, TTSConfig
from dotenv import load_dotenv
from fishaudio import FishAudio
from fishaudio.types import ReferenceAudio
from fishaudio.utils import save

load_dotenv()

api_key = os.getenv("FISH_API_KEY")

if not api_key:
    raise RuntimeError("FISH_API_KEY is missing from .env")

reference_path = Path("samples/original.wav")
output_path = Path("samples/replacement.wav")

reference_text = (
    "I built a small project called Speech Surgeon."
)

replacement_text = (
    "We launched the first version in June, "
    "and more than five thousand people tried it "
    "during the first week."
)

print("Loading reference audio...")

with open(reference_path, "rb") as f:
    reference_audio = f.read()

reference = ReferenceAudio(
    audio=reference_audio,
    text=reference_text,
)

print("Generating replacement speech with Fish S2.1 Pro...")
print()
print("Replacement text:")
print(replacement_text)
print()

client = FishAudio(api_key=api_key)

config = TTSConfig(
    format="wav",
)

audio = client.tts.convert(
    text=replacement_text,
    model="s2.1-pro",
    references=[reference],
    config=config,
)

save(audio, str(output_path))

print("Done.")
print(f"Created: {output_path}")