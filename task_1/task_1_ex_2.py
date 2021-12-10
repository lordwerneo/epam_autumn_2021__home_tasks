"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse as arg
import math
import operator


def calculate(args):
    function = getattr(math, args[0], None) or getattr(operator, args[0], None)
    if function is None:
        raise NotImplementedError
    else:
        if len(args) > 2:
            return function(type_converter(args[1]), type_converter(args[2]))
        else:
            try:
                return function(type_converter(args[1]))
            except TypeError:
                return args[1]


def type_converter(string_number):
    if string_number.isdigit():
        return int(string_number)
    else:
        return float(string_number)


def main():
    parser = arg.ArgumentParser()
    parser.add_argument('test_input', nargs='*')
    arguments = parser.parse_args()
    print(calculate(arguments.test_input))


if __name__ == '__main__':
    main()
