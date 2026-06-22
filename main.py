from stats import get_num_words, take_text, chars_dict_to_sorted_list
import sys

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    ruta = sys.argv[1]
    #ruta = "./books/frankenstein.txt" 
    texto = get_book_text(ruta)
    words = get_num_words(texto)
    num_characters = take_text(texto)
    count_charachters = chars_dict_to_sorted_list(num_characters)

    print_report(ruta, words, count_charachters)

# Filepath es ruta relativa al archivo que queremos pasar
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def print_report(path: str, word_count: dict[str, int], characters_count: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for charachter in characters_count:
        if charachter[0].isalpha():
            print(f"{charachter[0]}: {charachter[1]}")
    print("============= END ===============")

main()
