from IO.IO_module import read_input_lines
import json


def as_list(x) -> list:
    if type(x) == list:
        return x
    return [x]


def compare(item1, item2) -> int:
    if type(item1) == type(item2) == int:
        if item1 < item2:
            return -1
        elif item1 > item2:
            return 1
        return 0

    # Both must be list
    list1, list2 = as_list(item1), as_list(item2)
    while list1 and list2:
        elem1, elem2 = list1.pop(0), list2.pop(0)
        if (result := compare(elem1, elem2)) != 0:
            return result

    if (result := len(list1) - len(list2)) == 0:
        return 0
    return result // abs(result)


def main():
    input_lines = read_input_lines()

    cmp_list = [[], [], '']
    value = 0
    for index, line in enumerate(input_lines + ['']):
        position = index % 3
        if not line:
            if compare(cmp_list[0], cmp_list[1]) <= 0:
                value += index // 3 + 1
            continue
        cmp_list[position] = json.loads(line)

    print(f'{value=}')


if __name__ == '__main__':
    main()
