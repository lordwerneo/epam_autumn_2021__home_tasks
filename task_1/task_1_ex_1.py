"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse as arg


def calculate(operand_one, operator, operand_two):
    """Calculate the result based on operator and operands"""
    if operator == '/' and operand_two == 0:
        raise ZeroDivisionError
    elif operator == '/':
        return operand_one / operand_two
    elif operator == '*':
        return operand_one * operand_two
    elif operator == '+':
        return operand_one + operand_two
    else:
        return operand_one - operand_two


def type_converter(string_number):
    if "." in string_number:
        return float(string_number)
    else:
        return int(string_number)


def main():
    parser = arg.ArgumentParser()

    # Positional arguments
    parser.add_argument('operand_one')
    parser.add_argument('operator', type=str)
    parser.add_argument('operand_two')

    arguments = parser.parse_args()

    operators = ['+', '-', '/', '*']
    if arguments.operator not in operators:
        raise NotImplementedError('Test')
    else:
        operand_one = type_converter(arguments.operand_one)
        operand_two = type_converter(arguments.operand_two)
        print(calculate(operand_one, arguments.operator, operand_two))


if __name__ == '__main__':
    main()
