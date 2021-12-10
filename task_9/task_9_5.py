from typing import Dict


def count_letters(input_string: str) -> Dict[str, int]:
    """
    Count the frequency of occurrence of characters in the input string.
    :param input_string: String to look for characters in.
    :type input_string: str
    :return: Frequency of occurrence of characters in input string.
    :rtype: dict[str, int]
    """
    result = {}
    for item in input_string:
        if item.isalpha():
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
    return result


# print(count_letters('Hello world!') == {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})
