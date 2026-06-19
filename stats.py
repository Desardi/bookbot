def get_num_words( text: str) -> int:
    words = text.split()
    return len(words)

def take_text(text: str) -> dict[str, int]:
    characters: dict[str, int] = {}
    text_lower = text.lower()
    for character in text_lower:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters
