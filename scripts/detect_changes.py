from difflib import SequenceMatcher


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


if __name__ == "__main__":

    original_text = (
        "We launched the first version in March, "
        "and more than three thousand people tried it "
        "during the first week."
    )

    edited_text = (
        "We launched the first version in June, "
        "and more than five thousand people tried it "
        "during the first week."
    )

    changes = detect_changes(
        original_text,
        edited_text,
    )

    print()
    print("Detected changes")
    print("================")
    print()

    for change in changes:
        print(f"Original: {change['original']}")
        print(f"Edited:   {change['edited']}")
        print()