import os
import sys


def read_input_lines(root_file: os.path, file_name='input'):
    current_path = os.path.dirname(os.path.abspath(root_file))
    file_path = os.path.join(current_path, file_name)
    try:
        with open(file_path, 'r') as input_file:
            lines = input_file.read().splitlines()
    except FileNotFoundError:
        print(f'No such file or directory: \'{file_path}\'', file=sys.stderr)
        sys.exit(1)

    return lines
