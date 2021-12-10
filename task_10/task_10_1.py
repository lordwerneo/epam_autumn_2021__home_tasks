"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    """
    Read data from input file, sort and write to output file.
    :param input_file_path: Path to input file.
    :type input_file_path: file
    :param output_file_path: Path to output file.
    :type output_file_path: file
    """
    with open(input_file_path, 'r') as in_f, open(output_file_path, 'w') as out_f:
        out_f.writelines(sorted(in_f.readlines()))


# input_f, output_f = 'input1.txt', 'output1.txt'
# sort_names(input_f, output_f)