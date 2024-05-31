from collections import Counter

book_path = "books/frankenstein.txt"


def open_book(path: str):
    with open(path) as f:
        return f.read()


def count_words(book: str):
    return len(book.split())


def count_characters(book: str):
    return Counter(book.lower().strip())


def book_report(book: str):
    total_words = count_words(book)
    char_count = count_characters(book)

    print(f"--- Begin report of {book_path} ---", "\n")
    print(f"{total_words} words found in the document", "\n")

    for char in char_count:
        print(f"The {char} character was found {char_count[char]} times.")
    
    print("--- End report ---")


def main():
    book = open_book(book_path)
    book_report(book)


main()
