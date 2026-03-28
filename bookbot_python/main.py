from stats import (
    count_chars,
    count_words,
    map_list_to_dict,
    show_ordered_chars_count_list,
    sort_on,
)


def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def main():
    print("=" * 12 + " BOOKBOT " + "=" * 12)
    print("Analyzing book found at books/frankenstein.txt...")
    print("-" * 12 + " Word Count " + "-" * 12)

    content = get_book_text()
    words_number = count_words(content)
    print(f"Found {words_number} total words")
    print("-" * 12 + " Character Count" + "-" * 12)

    char_dict = count_chars(content)
    list_of_chars = map_list_to_dict(char_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    show_ordered_chars_count_list(list_of_chars)

    print("============= END ===============")


if __name__ == "__main__":
    main()
