def count_words(text: str) -> int:
    words = text.split()
    counter = len(words)
    return counter


def count_chars(text: str) -> dict:
    text = text.lower()
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] = chars[char] + 1

    return chars
