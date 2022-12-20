from IO.IO_module import read_input_lines
from functools import cmp_to_key
import json
from copy import deepcopy


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


def compare_copies(item1, item2) -> int:
    return compare(deepcopy(item1), deepcopy(item2))


def main():
    input_lines = read_input_lines() + ['[[2]]', '[[6]]']

    signals = []
    for index, line in enumerate(filter(lambda l: bool(l), input_lines)):
        signals.append(json.loads(line))

    signals_ordered = sorted(signals, key=cmp_to_key(compare_copies))
    decoder_key = (signals_ordered.index([[2]]) + 1) * (signals_ordered.index([[6]]) + 1)
    print(f'{decoder_key=}')


if __name__ == '__main__':
    main()
