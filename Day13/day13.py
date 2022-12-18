from IO.IO_module import read_input_lines
import json


def as_list(x) -> list:
    if type(x) is list:
        return x
    else:
        return [x]


def check_order(list1: list, list2: list):
    result = True
    for e1, e2 in zip(list1, list2):
        if type(e1) == type(e2) and type(e1) == int:
            result = result and e1 <= e2
        else:
            result = result and check_order(as_list(e1), as_list(e2))

    return result and len(list1) <= len(list2)


def main():
    input_lines = read_input_lines(file_name='test_input')

    cmp_list = [[], [], '']
    for index, line in enumerate(input_lines):
        position = index % 3
        if not line:
            print(f'{index // 3 + 1}, {check_order(cmp_list[0], cmp_list[1])}')
            continue
        cmp_list[position] = json.loads(line)


if __name__ == '__main__':
    main()
