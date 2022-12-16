from IO.IO_module import read_input_lines
import numpy as np


def check_far_away(knot1: np.ndarray, knot2: np.ndarray) -> np.ndarray:
    distance = knot1 - knot2
    if max(abs(distance)) > 1:
        return distance
    return np.array([])


def limit_move(move: np.ndarray) -> np.ndarray:
    signs = np.sign(move)
    return np.array([signs[0]*min(abs(move[0]), 1), signs[1]*min(abs(move[1]), 1)])


def main():
    input_lines = read_input_lines()
    rope = [np.zeros(2, dtype=int), np.zeros(2, dtype=int),
            np.zeros(2, dtype=int), np.zeros(2, dtype=int),
            np.zeros(2, dtype=int), np.zeros(2, dtype=int),
            np.zeros(2, dtype=int), np.zeros(2, dtype=int),
            np.zeros(2, dtype=int), np.zeros(2, dtype=int)]
    moves = {'L': np.array([0, -1]), 'U': np.array([1, 0]),
             'R': np.array([0, 1]), 'D': np.array([-1, 0])}

    t_positions = {(0, 0)}
    for line in input_lines:
        direction, amount = line.split()
        amount = int(amount)
        for _ in range(amount):
            rope[0] += moves[direction]
            for knot1, knot2 in zip(rope, rope[1:]):
                if (move := check_far_away(knot1, knot2)).size > 0:
                    knot2 += limit_move(move)
            t_positions.add((rope[-1][0], rope[-1][1]))

    print(f'{len(t_positions)=}')


if __name__ == '__main__':
    main()
