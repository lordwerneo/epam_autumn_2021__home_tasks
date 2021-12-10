""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse as arg


def check_formula(user_input):
    previous = False
    for index, element in enumerate(user_input[1:-1]):
        if element in ['+', '-'] and previous is True:
            return True
        elif not element.isdigit() and element not in ['+', '-']:
            return True
        elif element in ['+', '-']:
            previous = True
        else:
            previous = False
    return False


def main():
    parser = arg.ArgumentParser()
    parser.add_argument('user_input')
    arguments = parser.parse_args()
    if not arguments.user_input[0].isdigit() or not arguments.user_input[-1].isdigit():
        print((False, None))
    elif check_formula(arguments.user_input):
        print((False, None))
    else:
        result = eval(arguments.user_input)
        print((True, result))


if __name__ == '__main__':
    main()
