"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse as arg


def from_roman_numerals(roman_expression):
    roman_codes = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    if len(roman_expression) < 2:
        return roman_codes[roman_expression]

    # Convert roman digits into arabic digits.
    arabic_expression = [roman_codes[x.upper()] for x in roman_expression]

    negatives, positives = 0, arabic_expression[-1]
    for index, digit in enumerate(arabic_expression[:-1]):
        if digit < arabic_expression[index+1]:
            negatives += digit
        else:
            positives += digit

    return positives-negatives


def main():
    parser = arg.ArgumentParser()
    parser.add_argument('roman_expression', type=str)
    arguments = parser.parse_args()
    for digit in arguments.roman_expression:
        if digit not in ['I', 'V', 'X', 'L', 'C']:
            raise ValueError
    print(from_roman_numerals(arguments.roman_expression))


if __name__ == "__main__":
    main()
