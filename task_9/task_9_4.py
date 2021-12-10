from typing import List, Set
import string


def chars_in_all(*test_strings: List[str]) -> Set[str]:
    """
    Looking for unique characters among all input strings.
    :param test_strings: List of strings.
    :type test_strings: list[str]
    :return: Set of unique characters.
    :rtype: set[str]
    """
    sets = [set(i) for i in test_strings if isinstance(i, str)]
    if len(sets) != len(test_strings):
        raise TypeError
    return set.intersection(*sets)


def chars_in_one(*test_strings: List[str]) -> Set[str]:
    """
    Looking for all characters among all input strings.
    :param test_strings: List of strings.
    :type test_strings: list[str]
    :return: Set of all characters in list of input strings.
    :rtype: set[str]
    """
    sets = [set(i) for i in test_strings if isinstance(i, str)]
    if len(sets) != len(test_strings):
        raise TypeError
    return set.union(*sets)


def chars_in_two(*test_strings: List[str]) -> Set[str]:
    """
    Looking for all characters that appears at least in two words among all input strings.
    :param test_strings: List of strings.
    :type test_strings: list[str]
    :return: Set of characters that appears at least in two words.
    :rtype: set[str]
    """
    if len(test_strings) < 2:
        raise ValueError
    sets = [set(i) for i in test_strings if isinstance(i, str)]
    if len(sets) != len(test_strings):
        raise TypeError
    result = set()
    for i, first_set in enumerate(sets[:-1]):
        for second_set in sets[i+1:]:
            result.update(first_set.intersection(second_set))
    return result


def not_used_chars(*test_strings: List[str]) -> Set[str]:
    """
    Find all lower-case characters that weren't used among all input strings
    :param test_strings: List of strings.
    :type test_strings: list[str]
    :return: Set of lower-case characters that weren't used.
    :rtype: set[str]
    """
    sets = [set(i) for i in test_strings if isinstance(i, str)]
    if len(sets) != len(test_strings):
        raise TypeError
    return set(string.ascii_lowercase).difference(set.union(*sets))


# test = ['hello', 'world', 'python']
# print(chars_in_all(*test) == {'o'})
# print(chars_in_one(*test) == {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'})
# print(chars_in_two(*test) == {'h', 'l', 'o'})
# print(not_used_chars(*test) == {'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'})
