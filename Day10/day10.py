from IO.IO_module import read_input_lines


def main():
    input_lines = read_input_lines()

    exec_time = {'noop': 1, 'addx': 2}
    timestamps = [20, 60, 100, 140, 180, 220]
    cycles = 0
    signal_strength = 0
    x = 1

    for line in input_lines:
        cmd, *v = line.split()
        v = int(*v) if v else 0
        for _ in range(exec_time[cmd]):
            cycles += 1
            if cycles in timestamps:
                signal_strength += cycles * x
        x += v

    print(f'{signal_strength=}')


if __name__ == '__main__':
    main()
