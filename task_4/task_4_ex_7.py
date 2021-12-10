"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""

from typing import List
from math import prod


def product_array(num_list: List[int]) -> List[int]:
    result = []
    for index, _ in enumerate(num_list):
        temporary_num_list = num_list[:]
        del temporary_num_list[index]
        result.append(prod(temporary_num_list))
    return result
