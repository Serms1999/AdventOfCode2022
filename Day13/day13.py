from IO.IO_module import read_input_lines
import json


def as_list(x) -> list:
    if type(x) is list:
        return x
    else:
        return [x]


def compare_list(list1, list2) -> bool:
    while True:
        try:
            e1 = list1.pop(0)
            e2 = list2.pop(0)
        except IndexError:
            if len(list1) == 0:
                return len(list2) >= 0
            elif len(list2) == 0:
                return False

        if type(e1) == type(e2) == int:
            if e2 < e1:
                return False
        else:
            list_e1, list_e2 = as_list(e1), as_list(e2)
            if not compare_list(list_e1, list_e2):
                return False


def main():
    input_lines = read_input_lines(file_name='test_input')

    cmp_list = [[], [], '']
    value = 0
    for index, line in enumerate(input_lines + ['']):
        position = index % 3
        if not line:
            if compare_list(cmp_list[0], cmp_list[1]):
                value += index
                print(index // 3 + 1)
            continue
        cmp_list[position] = json.loads(line)

    print(f'{value=}')


if __name__ == '__main__':
    main()
