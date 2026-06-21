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

def sort_on(letra: tuple[str, int]) -> int:
    return letra[1]

def chars_dict_to_sorted_list(caracteres: dict[str, int]) -> list[tuple[str, int]]:
    letras: list[tuple[str, int]] = []
    for k in caracteres:
        letras.append((k, caracteres[k]))
    sorted_list = sorted(letras, reverse=True, key=sort_on)
    return sorted_list
