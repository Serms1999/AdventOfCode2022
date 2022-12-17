from IO.IO_module import read_input_lines


def main():
    input_lines = read_input_lines()

    exec_time = {'noop': 1, 'addx': 2}
    cycles = 0
    x = 1

    for line in input_lines:
        cmd, *v = line.split()
        v = int(*v) if v else 0
        for _ in range(exec_time[cmd]):
            pixel = '#' if x in range((cycles % 40) - 1, (cycles % 40) + 2) else '.'
            print(pixel, end='')
            cycles += 1
            if cycles % 40 == 0:
                print()
        x += v


if __name__ == '__main__':
    main()
