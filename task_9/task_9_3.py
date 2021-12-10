import re


def get_longest_word(s: str) -> str:
    """
    Find the longest word in a string.
    :param s: String to look for a word in.
    :type s: str
    :return: Longest word.
    :rtype: str
    """
    if not isinstance(s, str):
        raise ValueError
    longest_word, longest_word_length = '', 0
    for word in re.findall(r'\S+', s):
        if len(word) > longest_word_length:
            longest_word, longest_word_length = word, len(word)
    return longest_word


# print(get_longest_word('/Lorem .ipsum /dolor ^sit amet, consectetur adipiscing elit. '
#                        'Suspendisse blandit justo non ex maximus tempus'))
