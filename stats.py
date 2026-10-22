def count_words(text: str) -> int:
    return len(text.split())

def character_count(text: str) -> dict[str, int]:
    count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in count:
            count[lower_char] = count.get(lower_char) + 1
        else:
            count[lower_char] = 1
    
    return count

def sort_on(count_tuple: tuple[str, int]) -> int:
    return count_tuple[1];

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    res = []
    for key in char_count.keys():
        tuple = (key, char_count[key])
        res.append(tuple)

    sorted_res = sorted(res, reverse=True, key=sort_on)
    return sorted_res
