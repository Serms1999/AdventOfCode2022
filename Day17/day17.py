from IO.IO_module import read_input_lines


rock_patterns = ('-', '+', '⅃', '|', '■')
moves = {'>': (1, 0), '<': (-1, 0), 'down': (0, -1)}


def sum_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum,zip(a, b)))


def new_rock(cur_rock: str) -> str:
    index = rock_patterns.index(cur_rock)
    index = (index + 1) % len(rock_patterns)
    return rock_patterns[index]


def rock_checks(rock: str) -> list:
    if rock == '-':
        return [(i, 0) for i in range(4)]
    if rock == '+':
        return [(0, 1), (1, 0), (1, 2), (2, 1)]
    if rock == '⅃':
        return [(i, 0) for i in range(3)]
    if rock == '|':
        return [(0, i) for i in range(4)]
    return [(0, 0), (1, 0), (0, 1), (1, 1)]


def rock_height(rock: str) -> list:
    if rock == '-':
        return [(i, 1) for i in range(4)]
    if rock == '+':
        return [(0, 2), (1, 3), (2, 2)]
    if rock == '⅃':
        return [(1, 3)]
    if rock == '|':
        return [(0, 4)]
    return [(0, 2), (1, 2)]


def check_pos(pos: tuple, checks: list, column_height: dict) -> int:
    #############################################################
    # 0 -> MOVABLE                                              #
    # 1 -> OUT OF WALLS                                         #
    # 2 -> REST                                                 #
    #############################################################

    new_checks = [sum_tuples(pos, check) for check in checks]
    if not all(check[0] in range(7) for check in new_checks):
        return 1
    elif not all(check != (check[0], column_height[check[0]]) for check in new_checks):
        return 2

    return 0


def move_rock(cur_rock: str, pos: [int, int], move: str, column_height: dict) -> int:
    checks = rock_checks(cur_rock)
    new_pos = sum_tuples(pos, moves[move])

    ret = check_pos(new_pos, checks, column_height)
    if ret == 0:
        pos[0] = new_pos[0]
        pos[1] = new_pos[1]
        return 0
    elif ret == 2:
        new_heights = [(pos[0] + h[0], h[1]) for h in rock_height(cur_rock)]
        for new_height in new_heights:
            column_height[new_height[0]] += new_height[1]
        return 2
    return 1


def main():
    jets = read_input_lines(file_name='test_input')[0]
    column_height = {i: -1 for i in range(7)}
    jet_index = 0
    prev_rock = '■'

    for index in range(2022):
        cur_rock = new_rock(prev_rock)
        pos = [2, max(column_height.values()) + 4]
        while True:
            move_rock(cur_rock, pos, jets[jet_index], column_height)
            jet_index = (jet_index + 1) % len(jets)

            ret = move_rock(cur_rock, pos, 'down', column_height)
            if ret == 2:
                break

        prev_rock = cur_rock

    print(column_height)


if __name__ == '__main__':
    main()
