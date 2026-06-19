def main() -> None:
    ruta = "./books/frankenstein.txt" 
    texto = get_book_text(ruta)
    print(texto)

# Filepath es ruta relativa al archivo que queremos pasar
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
    return f.read()

def word_count(text: str) -> int:
    words = text.split()
    pass

main()
