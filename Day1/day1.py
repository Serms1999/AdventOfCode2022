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

    # Last element
    if current_sum > max_sum:
        max_sum = current_sum

    return max_sum


def get_three_top_elves(input_lines: list) -> int:
    biggest_sums = []
    current_sum = 0
    for cal in input_lines:
        if cal != '':
            current_sum += int(cal)
        else:
            if len(biggest_sums) < 3:
                biggest_sums.append(current_sum)
            elif current_sum > biggest_sums[0]:
                biggest_sums[0] = current_sum
            biggest_sums.sort()
            current_sum = 0

    # Last element
    if len(biggest_sums) < 3:
        biggest_sums.append(current_sum)
    elif current_sum > biggest_sums[0]:
        biggest_sums[0] = current_sum

    return sum(biggest_sums)


def main():
    input_lines = read_input_lines()
    print(get_three_top_elves(input_lines))


if __name__ == '__main__':
    main()
