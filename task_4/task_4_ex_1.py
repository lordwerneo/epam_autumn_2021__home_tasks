"""04 Task 1.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa. The
function should return modified string.
Usage of any replacing string functions is prohibited.
"""


def swap_quotes(string: str) -> str:
    result, replace = '', {'"': "'", "'": '"'}
    for char in string:
        if char in replace:
            result += replace[char]
        else:
            result += char
    return result

