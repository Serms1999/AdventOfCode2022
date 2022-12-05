from IO.IO_module import read_input_lines


def get_max_elf(input_lines: list) -> int:
    max_sum = 0
    current_sum = 0
    for cal in input_lines:
        if cal != '':
            current_sum += int(cal)
        else:
            if current_sum > max_sum:
                max_sum = current_sum
            current_sum = 0

    return max_sum


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(get_max_elf(input_lines))


if __name__ == '__main__':
    main()