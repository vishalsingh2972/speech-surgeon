from difflib import SequenceMatcher


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


ORIGINAL_START = 4.32
ORIGINAL_END = 10.08


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


changes = detect_changes(
    ORIGINAL_TEXT,
    EDITED_TEXT,
)


print()
print("Surgery plan")
print("============")
print()

print(
    f"Original audio region: "
    f"{ORIGINAL_START:.2f}s → {ORIGINAL_END:.2f}s"
)

print()

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