def count_words(text: str) -> int:
    words = text.split()
    counter = len(words)
    return counter


def count_chars(text: str) -> dict:
    text = text.lower()
    chars = {}
    for char in text:
        chars[char] = chars.get(char, 0) + 1

    return chars
