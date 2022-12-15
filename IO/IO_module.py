import os
import sys
import inspect


def read_input_lines(file_name='input'):
    caller_file = inspect.getouterframes(inspect.currentframe(), 2)[1][1]
    current_path = os.path.dirname(caller_file)
    file_path = os.path.join(current_path, file_name)
    try:
        with open(file_path, 'r') as input_file:
            lines = input_file.read().splitlines()
    except FileNotFoundError:
        print(f'No such file or directory: \'{file_path}\'', file=sys.stderr)
        sys.exit(1)

    return lines
