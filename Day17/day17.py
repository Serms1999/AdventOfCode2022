from IO.IO_module import read_input_lines


rock_patterns = ('-', '+', '⅃', '|', '■')


def sum_tuples(a: (int, int), b: (int, int)) -> (int, int):
    return tuple(map(sum,zip(a, b)))


def new_rock(cur_rock: str) -> str:
    index = rock_patterns.index(cur_rock)
    index = (index + 1) % len(rock_patterns)
    return rock_patterns[index]


def rock_checks(rock: str) -> list:
    if rock == '-':
        return [(i, 0) for i in range(4)]
    if rock == '+':
        return [(-1, 1), (0, 0), (1, 1)]
    if rock == '⅃':
        return [(i, 0) for i in range(3)]
    if rock == '|':
        return [(0, 0)]
    return [(0, 0), (1, 0)]


def check_pos(pos: (int, int), checks: list, column_height: dict) -> int:
    #############################################################
    # 0 -> MOVABLE                                              #
    # 1 -> OUT OF WALLS                                         #
    # 2 -> REST                                                 #
    #############################################################
    new_checks = [sum_tuples(pos, check) for check in checks]
    for check in new_checks:
        if check[0] not in range(7):
            return 1
        elif check == (check[0], column_height[check[0]] + 1):
            return 2

    return 0


def move_rock(cur_rock: str, pos: (int, int), move: str, column_height: dict) -> int:
    checks = rock_checks(cur_rock)
    if move == '>':
        ret = check_pos(sum_tuples(pos, (1, 0)), checks, column_height)
        if ret == 0:
            new_checks = [sum_tuples(pos, check) for check in checks]
    elif move == '<':
        ret = check_pos(sum_tuples(pos, (-1, 0)), checks, column_height)
        if ret == 0:
            print()
    else:
        ret = check_pos(sum_tuples(pos, (0, -1)), checks, column_height)
        if ret == 0:
            print()
        elif ret == 2:
            print()


def main():
    jets = read_input_lines(file_name='test_input')[0]
    column_height = {i: 0 for i in range(7)}
    jet_index = 0

    for index in range(2022):
        cur_rock = rock_patterns[index]
        pos = (2, 3)
        while True:

            move_rock(cur_rock, pos, jets[jet_index], column_height)
            jet_index = (jet_index + 1) % len(jets)

            ret = move_rock(cur_rock, pos, 'down', column_height)

            if ret == 2:
                break


if __name__ == '__main__':
    main()
