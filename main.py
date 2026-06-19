from stats import get_num_words, take_text

def main() -> None:
    ruta = "./books/frankenstein.txt" 

    texto = get_book_text(ruta)
    words = get_num_words(texto)
    num_characters = take_text(texto)

    print(f"Found {words} total words")
    print(num_characters)
    #for k in num_characters:
    #    print(f"'{k}': {num_characters[k]}")


# Filepath es ruta relativa al archivo que queremos pasar
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

main()
