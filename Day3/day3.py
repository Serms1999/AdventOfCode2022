from IO.IO_module import read_input_lines


def get_compartments(input_lines: list) -> list:
    compartments = []
    for line in input_lines:
        half_length = len(line) // 2
        half1, half2 = line[:half_length], line[half_length:]
        compartments.append((set(half1), set(half2)))

    return compartments


def get_repeated_items(compartments: list) -> list:
    repeated_items = []
    for half1, half2 in compartments:
        common_item = half1.intersection(half2).pop()
        repeated_items.append(common_item)

    return repeated_items


def calculate_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


def main():
    input_lines = read_input_lines(root_file=__file__)
    compartments = get_compartments(input_lines)
    repeated_items = get_repeated_items(compartments)
    sum_priority = sum(map(lambda i: calculate_priority(i), repeated_items))
    print(f'{sum_priority=}')


if __name__ == '__main__':
    main()
