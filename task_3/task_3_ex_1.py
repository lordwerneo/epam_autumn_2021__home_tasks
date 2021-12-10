"""Task 1
For a given integer n calculate the value which is equal to a:
- squared number, if its value is strictly positive;
- modulus of a number, if its value is strictly negative;
- zero, if the integer n is zero.

Example,
n = 4 result = 16
n = -5 result = 5
n = 0 result = 0

Example of how the task should be called:
python3 task_3_ex_1.py 4

Note: use argparse module for parsing arguments from CLI
"""
import argparse as arg


def calculate(n):
    if n > 0:
        return n ** 2
    elif n < 0:
        return n * -1
    else:
        return 0


def main():
    parser = arg.ArgumentParser()
    parser.add_argument("n", type=int)
    arguments = parser.parse_args()
    print(calculate(arguments.n))


if __name__ == '__main__':
    main()
