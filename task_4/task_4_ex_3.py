"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str = None, delimiter: str = None) -> list:
    if isinstance(str_to_split, str) and isinstance(delimiter, str):
        if delimiter not in str_to_split:
            return [str_to_split]
        result, start = [], 0
        for index, char in enumerate(str_to_split):
            if char == delimiter:
                result.append(str_to_split[start:index])
                start = index + 1
        result.append(str_to_split[start:index + 1])
        return result
    else:
        raise ValueError



