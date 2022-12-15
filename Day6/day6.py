from IO.IO_module import read_input_lines


def main():
    input_lines = read_input_lines()
    for input_line in input_lines:
        possible_markers = [input_line[i:i + 14] for i in range(len(input_line) - 13)]
        for index, possible_marker in enumerate(possible_markers):
            if len(set(possible_marker)) == 14:
                break
        print(f'{index+14=}, {possible_marker=}')


if __name__ == '__main__':
    main()
