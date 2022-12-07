from IO.IO_module import read_input_lines


def rock_paper_scissors(own_choice: str, opponent_choice) -> str:
    if own_choice == opponent_choice:
        return 'draw'
    res = (ord(own_choice) - ord(opponent_choice)) % 3
    if res == 1:
        return 'win'
    return 'defeat'


def strategy_guide(input_lines: list) -> int:
    games = [e.split() for e in input_lines]

    map_own_choice = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    map_choice = {'X': 1, 'Y': 2, 'Z': 3}
    map_result = {'win': 6, 'draw': 3, 'defeat': 0}

    total_points = 0
    for opponent_choice, own_choice in games:
        res = rock_paper_scissors(map_own_choice[own_choice], opponent_choice)
        points = map_choice[own_choice] + map_result[res]
        total_points += points

    return total_points


def main():
    input_lines = read_input_lines(root_file=__file__)
    print(f'Expected points: {strategy_guide(input_lines)}')


if __name__ == '__main__':
    main()
