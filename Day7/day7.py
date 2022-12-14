from IO.IO_module import read_input_lines
import re


def parse_file_system(commands: list) -> dict:
    dirs = {}
    dir_files = {}
    parent_dir, current_dir = [], ''
    pat_cd = re.compile(pattern=r'\$ cd (.*)')
    pat_dir = re.compile(pattern=r'dir (.*)')
    pat_file = re.compile(pattern=r'([0-9]+) (.*)')
    for cmd in commands:
        if mat := re.match(pattern=pat_cd, string=cmd):
            if current_dir:
                parent_dir.append(current_dir)
                current_dir = mat.group(1)
                dirs[parent_dir[-1]].append(current_dir)
            else:
                current_dir = mat.group(1)
                dir_files[current_dir] = []
            dirs[current_dir] = []

        elif mat := re.match(pattern=pat_dir, string=cmd):
            dir_name = mat.group(1)
            dirs[current_dir].append(dir_name)
            dir_files[dir_name] = []
        elif mat := re.match(pattern=pat_file, string=cmd):
            dir_files[current_dir].append((mat.group(2), mat.group(1)))

    print(f'{dirs=}, {dir_files=}')


def main():
    input_lines = read_input_lines(root_file=__file__, file_name='test_input')
    file_system = parse_file_system(input_lines)
    print(file_system)


if __name__ == '__main__':
    main()
