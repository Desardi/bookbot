from stats import get_num_words

def main() -> None:
    ruta = "./books/frankenstein.txt" 

    texto = get_book_text(ruta)
    words = get_num_words(texto)

    print(f"Found {words} total words")

# Filepath es ruta relativa al archivo que queremos pasar
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

main()
