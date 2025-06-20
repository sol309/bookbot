import sys
from stats import num_words
from stats import get_number_of_characters
from stats import sort_dictionary
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    words = num_words(book)
    print("Analyzing book found at %s")

    print(f"Found {words} total words")
    
    characters = get_number_of_characters(book)
    frequencies = sort_dictionary(characters)
    for letter in frequencies:
        if letter["char"].isalpha():
            print( f"{letter["char"]}: {letter["num"]}")
main()
