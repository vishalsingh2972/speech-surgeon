from difflib import SequenceMatcher

from find_target import find_target


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


print()
print("Surgery plan")
print("============")
print()

print("Finding target sentence...")

target = find_target(
    "samples/original.wav",
    TARGET_WORDS,
)

original_start = target["start"]
original_end = target["end"]

print(
    f"Original audio region: "
    f"{original_start:.2f}s → {original_end:.2f}s"
)

print()

changes = detect_changes(
    ORIGINAL_TEXT,
    EDITED_TEXT,
)

print("Detected edits:")

for change in changes:
    print(
        f"- {change['original']} "
        f"→ {change['edited']}"
    )

print()

print("Replacement text:")
print(EDITED_TEXT)

print()

print("Ready for voice reconstruction.")