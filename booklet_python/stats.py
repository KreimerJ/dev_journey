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


def map_list_to_dict(dictionary: dict) -> list[dict]:
    sorted_list = []

    for key, value in dictionary.items():
        sorted_list.append({"char": key, "num": value})

    return sorted_list


def sort_on(item: dict):
    return item["num"]


def show_ordered_chars_count_list(list_of_chars):
    for i in range(len(list_of_chars)):
        if not list_of_chars[i]["char"].isalpha():
            pass
        else:
            print(f"{list_of_chars[i]['char']}: {list_of_chars[i]['num']}")
