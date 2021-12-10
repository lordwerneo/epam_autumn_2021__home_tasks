"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""

from typing import List
import re


def most_common_words(file_path: str, top_words: int) -> List[str]:
    """
    Returns the most common words in the given file.
    :param file_path: Path to the text file.
    :type file_path: file
    :param top_words: Number of most common words to be returned.
    :type top_words: int
    :return: Most common words.
    :rtype: list[str]
    """
    result = {}
    with open(file_path, 'r') as f:
        for line in f:
            for word in re.findall(r"[a-zA-Z']+", line):
                if word.lower() in result:
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
    result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in result[:top_words]]


# print(most_common_words('input2.txt', 5))
