"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""
import decimal


def sum_odd_numbers(n: int) -> int:
    if isinstance(n, int) and n > 0:
        result = 0
        for digit in str(n):
            if digit.isnumeric() and int(digit) % 2 == 1:
                result += int(digit)
            elif not digit.isnumeric():
                raise TypeError
        return result
    else:
        raise TypeError


def sum_odd_number_two(n: int) -> int:
    if isinstance(n, int) and n > 0 and not isinstance(n, bool):
        return sum([int(x) for x in str(n) if int(x) % 2 == 1])
    raise TypeError


print(sum_odd_number_two(12345))
