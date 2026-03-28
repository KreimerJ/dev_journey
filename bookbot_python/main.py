import sys

from stats import (
    count_chars,
    count_words,
    map_list_to_dict,
    show_ordered_chars_count_list,
    sort_on,
)


def get_book_text(path: str):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main(book_path):

    content = get_book_text(book_path)
    words_number = count_words(content)
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print(f"Analyzing book found at {book_path}")
    print("-" * 12 + " Word Count " + "-" * 12)
    print(f"Found {words_number} total words")
    print("-" * 12 + " Character Count" + "-" * 12)

    char_dict = count_chars(content)
    list_of_chars = map_list_to_dict(char_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    show_ordered_chars_count_list(list_of_chars)

    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    main(book_path)
