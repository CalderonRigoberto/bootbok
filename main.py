import sys
from stats import count_words, character_count, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    content = get_book_text(sys.argv[1])
    total_words = count_words(content)
    char_count = character_count(content)
    sorted_chars_count_list = chars_dict_to_sorted_list(char_count) 
    print_book_report(total_words, sorted_chars_count_list)



def get_book_text(path_file: str) -> str:
    file_contents = ""
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents


def print_book_report(total_words: int, sorted_chars_count_list: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for sorted_char_count in sorted_chars_count_list:
        if sorted_char_count[0].isalpha():
           print(f"{sorted_char_count[0]}: {sorted_char_count[1]}")
    print("============= END ===============")

main()
