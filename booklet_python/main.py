from stats import count_words


def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def main():
    content = get_book_text()
    words_number = count_words(content)
    print(f"Found {words_number} total words")


if __name__ == "__main__":
    main()
