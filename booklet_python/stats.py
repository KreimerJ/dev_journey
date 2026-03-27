def count_words(text: str) -> int:
    words = text.split()
    counter = len(words)
    return counter


def count_chars(txt: str) -> dict:
    txt = txt.lower()
    chars = {}
    for char in txt:
        if char not in chars:
            chars[char] = [char]
        else:
            chars[char].append(char)

    for char in chars:
        chars[char] = len(chars[char])

    return chars
