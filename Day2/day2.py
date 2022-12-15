from IO.IO_module import read_input_lines


def rock_paper_scissors(own_choice: str, opponent_choice: str) -> str:
    if own_choice == opponent_choice:
        return 'draw'
    res = (ord(own_choice) - ord(opponent_choice)) % 3
    if res == 1:
        return 'win'
    return 'defeat'


def rock_paper_scissors_inverse(expectation: str, opponent_choice: str) -> str:
    options = {'defeat': -1, 'draw': 0, 'win': 1}
    opponent_choice_normalized = ord(opponent_choice) - ord('A')
    own_choice_normalized = (opponent_choice_normalized + options[expectation]) % 3
    return chr(own_choice_normalized + ord('X'))


def strategy_guide(input_lines: list) -> int:
    games = [e.split() for e in input_lines]

    map_own_choice = {'X': 'defeat', 'Y': 'draw', 'Z': 'win'}
    map_choice = {'X': 1, 'Y': 2, 'Z': 3}
    map_result = {'win': 6, 'draw': 3, 'defeat': 0}

    total_points = 0
    for opponent_choice, own_choice in games:
        own_choice_mapped = map_own_choice[own_choice]
        res = rock_paper_scissors_inverse(own_choice_mapped, opponent_choice)
        points = map_choice[res] + map_result[own_choice_mapped]
        total_points += points

    return total_points


def main():
    input_lines = read_input_lines()
    print(f'Expected points: {strategy_guide(input_lines)}')


if __name__ == '__main__':
    main()
