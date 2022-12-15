from IO.IO_module import read_input_lines
import re


def check_contained(line: str) -> int:
    line_RE = r'([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)'

    match = re.search(line_RE, line)
    a1, a2, b1, b2 = [int(match.group(i)) for i in range(1, 5)]
    elf1 = [e in range(a1, a2 + 1) for e in range(1, 100 + 1)]
    elf2 = [e in range(b1, b2 + 1) for e in range(1, 100 + 1)]
    and_array = [e1 and e2 for e1, e2 in zip(elf1, elf2)]

    return any(and_array)


def main():
    input_lines = read_input_lines()
    print(sum([check_contained(line) for line in input_lines]))


if __name__ == '__main__':
    main()
