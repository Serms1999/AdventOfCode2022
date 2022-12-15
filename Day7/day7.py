from IO.IO_module import read_input_lines
import re


def parse_file_system(commands: list) -> dict:
    root = {}
    current_dir = {}
    parent_dirs = []
    pat_cd = re.compile(pattern=r'\$ cd (.*)')
    pat_dir = re.compile(pattern=r'dir (.*)')
    pat_file = re.compile(pattern=r'([0-9]+) (.*)')
    for cmd in commands:
        if mat := pat_cd.match(cmd):
            if not current_dir:
                # '$ cd /'
                root = current_dir
                continue
            elif (dir_name := mat.group(1)) == '..':
                current_dir = parent_dirs.pop()
            else:
                parent_dirs.append(current_dir)
                current_dir = current_dir[dir_name]
        elif mat := pat_dir.match(cmd):
            current_dir[mat.group(1)] = {}
        elif mat := pat_file.match(cmd):
            current_dir[mat.group(2)] = int(mat.group(1))

    return root


def get_dir_size(root: dict, dirs: list) -> int:
    value = 0
    for name, item in root.items():
        if type(item) == int:
            value += item
        else:
            dir_value = get_dir_size(item, dirs)
            dirs.append(dir_value)
            value += dir_value

    return value


def main():
    input_lines = read_input_lines()
    root = parse_file_system(input_lines)

    dir_size = []
    used_space = get_dir_size(root, dir_size)
    unused_space = 70_000_000 - used_space

    big_enough_dirs = list(filter(lambda s: unused_space + s >= 30_000_000, dir_size))
    print(f'{sorted(big_enough_dirs)[0]=}')


if __name__ == '__main__':
    main()
