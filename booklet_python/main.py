def get_book_text():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def main():
    lines = get_book_text()
    print(lines)


if __name__ == "__main__":
    main()
