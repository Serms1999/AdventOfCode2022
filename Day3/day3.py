from IO.IO_module import read_input_lines


def group_elves(elves_list: list) -> list:
    elves_grouped = []
    for index, elf in enumerate(elves_list):
        if index % 3 == 0:
            elves_grouped.append([])
        elves_grouped[index // 3].append(set(elf))

    return elves_grouped


def get_compartments(rucksacks: list) -> list:
    compartments = []
    for line in rucksacks:
        half_length = len(line) // 2
        half1, half2 = line[:half_length], line[half_length:]
        compartments.append((set(half1), set(half2)))

    return compartments


def get_repeated_items(compartments: list) -> list:
    repeated_items = []
    for half1, half2 in compartments:
        common_item = (half1 & half2).pop()
        repeated_items.append(common_item)

    return repeated_items


def get_repeated_items_by_group(groups: list) -> list:
    repeated_items = []
    for group in groups:
        common_item = set.intersection(*group).pop()
        repeated_items.append(common_item)

    return repeated_items


def calculate_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


def main():
    input_lines = read_input_lines()
    groups = group_elves(input_lines)
    repeated_items = get_repeated_items_by_group(groups)
    sum_priority = sum(map(lambda i: calculate_priority(i), repeated_items))
    print(f'{sum_priority=}')


if __name__ == '__main__':
    main()
