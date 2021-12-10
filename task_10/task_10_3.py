"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv
from typing import List


def get_top_performers(file_path: str, number_of_top_students: int=5) -> List[str]:
    """
    Find top performers in the input .csv file.
    :param file_path: Path to input .csv file.
    :type file_path: str
    :param number_of_top_students: Number of top performers to return.
    :type number_of_top_students: int
    :return: Top performers.
    :rtype: list[str]
    """
    with open(file_path, 'r') as f_in:
        csv_reader = csv.reader(f_in)
        next(csv_reader)
        csv_reader_sorted = sorted(csv_reader, key=lambda x: x[2], reverse=True)
    return [x[0] for x in csv_reader_sorted[:number_of_top_students]]


def write_students_age_desc(file_path: str, output_file: str) -> None:
    """
    Sort students from input .csv file and write them to output .csv file.
    :param file_path: Path to the file to read from.
    :type file_path: str
    :param output_file: Path to the file to write to.
    :type output_file: str
    :return: None
    """
    with open(file_path, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
        csv_reader = csv.reader(f_in)
        csv_reader_sorted = sorted(csv_reader, key=lambda x: x[1], reverse=True)
        csv_writer = csv.writer(f_out)
        csv_writer.writerows(csv_reader_sorted)


# in_file, out_file = 'input3.csv', 'output3.csv'
# print(get_top_performers(in_file))
# write_students_age_desc(in_file, out_file)
