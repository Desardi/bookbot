def main() -> None:
    ruta = "./books/frankenstein.txt" 
    texto = get_book_text(ruta)
    words = word_count(texto)

    print(f"Found {words} total words")


# Filepath es ruta relativa al archivo que queremos pasar
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def word_count(text: str) -> int:
    words = text.split()
    return len(words)

main()
