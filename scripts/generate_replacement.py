import os
from pathlib import Path

from dotenv import load_dotenv
from fishaudio import FishAudio
from fishaudio.types import ReferenceAudio, TTSConfig
from fishaudio.utils import save


load_dotenv()


API_KEY = os.getenv("FISH_API_KEY")

if not API_KEY:
    raise RuntimeError("FISH_API_KEY is missing from .env")


REFERENCE_PATH = Path("samples/original.wav")
OUTPUT_PATH = Path("samples/replacement.wav")


REFERENCE_TEXT = (
    "I built a small project called Speech Surgeon."
)

EDITED_TEXT = (
    "We launched the first version in June, "
    "and more than five thousand people tried it "
    "during the first week."
)


print("Speech Surgeon")
print("================")
print()
print("Generating replacement speech...")
print()
print("Replacement text:")
print(EDITED_TEXT)
print()


with open(REFERENCE_PATH, "rb") as f:
    reference_audio = f.read()


reference = ReferenceAudio(
    audio=reference_audio,
    text=REFERENCE_TEXT,
)


client = FishAudio(
    api_key=API_KEY,
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
    str(OUTPUT_PATH),
)


print("Done.")
print(f"Created: {OUTPUT_PATH}")