import re


def is_palindrome(input_string: str) -> bool:
    """
    Check if input string is palindrome.
    :param input_string: string to check
    :type input_string: str
    :return: True or False based on result.
    :rtype: bool
    """
    if not isinstance(input_string, str):
        raise ValueError
    stripped_input = re.sub(r'\W', '', input_string).lower()
    return stripped_input == ''.join(reversed(stripped_input))


# print(is_palindrome('A nut for a jar of tuna.'))
# print(is_palindrome('Are we not pure? “No, sir!” Panama’s moody Noriega brags. “It is garbage!” '
#                     'Irony dooms a man—a prisoner up to new era.'))
# print(is_palindrome('2-20-22 '))