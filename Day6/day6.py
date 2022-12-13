from IO.IO_module import read_input_lines


def main():
    input_line = read_input_lines(root_file=__file__)[0]
    possible_markers = [input_line[i:i + 4] for i in range(len(input_line) - 3)]
    for index, possible_marker in enumerate(possible_markers):
        if len(set(possible_marker)) == 4:
            break
    print(f'{index+4=}, {possible_marker=}')


if __name__ == '__main__':
    main()
