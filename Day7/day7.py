from IO.IO_module import read_input_lines
import re


def parse_file_system(commands: list) -> (dict, dict):
    dirs = {}
    dir_files = {}
    parent_dir, current_dir = [], ''
    pat_cd = re.compile(pattern=r'\$ cd (.*)')
    pat_dir = re.compile(pattern=r'dir (.*)')
    pat_file = re.compile(pattern=r'([0-9]+) (.*)')
    for cmd in commands:
        if mat := pat_cd.match(cmd):
            if not current_dir:
                current_dir = mat.group(1)
                dirs[current_dir] = []
                dir_files[current_dir] = []
            else:
                dir_name = mat.group(1)
                if dir_name == '..':
                    current_dir = parent_dir.pop()
                else:
                    parent_dir.append(current_dir)
                    current_dir = dir_name

        elif mat := pat_dir.match(cmd):
            dir_name = mat.group(1)
            dirs[current_dir].append(dir_name)
            dirs[dir_name] = []
            dir_files[dir_name] = []
        elif mat := pat_file.match(cmd):
            dir_files[current_dir].append((mat.group(2), int(mat.group(1))))

    return dirs, dir_files


def get_dir_size(dir_name: str, dirs: dict, dir_files: dict) -> dict:
    files_size = sum([size for _, size in dir_files[dir_name]])
    subdir_size = sum([get_dir_size(subdir, dirs, dir_files) for subdir in dirs[dir_name]])
    return files_size + subdir_size


def main():
    input_lines = read_input_lines(root_file=__file__)
    dirs, dir_files = parse_file_system(input_lines)

    dir_size = {dir_name: get_dir_size(dir_name, dirs, dir_files) for dir_name in dirs}
    big_dirs = dict(filter(lambda d: d[1] <= 100_000, dir_size.items()))
    print(f'{sum(big_dirs.values())=}')


if __name__ == '__main__':
    main()
