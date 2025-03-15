from stats import *


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    dic = counting_characters(text)
    sorted_char = sorted_count(dic)
    for entry in sorted_char:
        print(f"'{entry['character']}': {entry['count']}")
    print("============= END ===============")

main()
