def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def words_counter(text: str) -> int:
    words = text.split()
    counter = len(words)

    return counter


def main():
    content = get_book_text()
    words_number = words_counter(content)
    print(f"Found {words_number} total words")


if __name__ == "__main__":
    main()
