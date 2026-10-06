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
            "original": " ".join(
                original_words[i1:i2]
            ),
            "edited": " ".join(
                edited_words[j1:j2]
            ),
        })

    return changes


def find_changed_sentence(original, edited):
    original_sentences = [
        sentence.strip()
        for sentence in original.split(".")
        if sentence.strip()
    ]

    edited_sentences = [
        sentence.strip()
        for sentence in edited.split(".")
        if sentence.strip()
    ]

    for index, original_sentence in enumerate(
        original_sentences
    ):
        if index >= len(edited_sentences):
            continue

        edited_sentence = edited_sentences[index]

        if original_sentence != edited_sentence:
            return {
                "original": original_sentence,
                "edited": edited_sentence,
            }

    return None