"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum


class SortOrder(Enum):
    ascending = 'ascending'
    descending = 'descending'


def is_sorted(num_list: list[int], sort_order: SortOrder) -> bool:
    """
    Check if the list has a correct sort order.
    :param num_list: The list to check for an order.
    :type num_list: list[int]
    :param sort_order: Order of a list, descending or ascending.
    :type sort_order: SortOrder
    :return: True if the order of the list is correct, and False if it is not.
    :rtype: bool
    """
    for i in range(len(num_list)):
        if i == 0:
            continue
        if sort_order == SortOrder.ascending and num_list[i] < num_list[i - 1]:
            return False
        elif sort_order is SortOrder.descending and num_list[i] > num_list[i - 1]:
            return False
    return True


def transform(num_list: list[int], sort_order: SortOrder) -> list[int]:
    """
    Function to transform input list if it's has correct order.
    :param num_list: The list to transform.
    :type num_list: list[int]
    :param sort_order: Order of a list, descending or ascending.
    :type sort_order: SortOrder
    :return: Return transformed list if it has correct order, or the input list if it doesn't.
    :rtype: list[int]
    """
    if (not isinstance(num_list, list) or not all(isinstance(x, int) for x in num_list)
            or not isinstance(sort_order, SortOrder)) or not num_list:
        raise TypeError
    return [i + number for i, number in enumerate(num_list)] if is_sorted(num_list, sort_order) else num_list




# sort_order = 'ascending'
# print(SortOrder.ascending)
# print(sort_order == SortOrder.ascending)
#
# test_list = [1, 2, 3, 4, 5, 't']
# print(all(isinstance(x, int) for x in test_list))

# if __name__ == '__main__':
#     print(transform([5, 17, 24, 88, 33, 2], SortOrder.ascending))
#     print(transform([15, 10, 3], SortOrder.ascending))
#     print(transform([15, 10, 3], SortOrder.descending))
#     print(transform([], SortOrder.ascending))
