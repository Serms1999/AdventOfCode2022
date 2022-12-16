from IO.IO_module import read_input_lines
import numpy as np


def check_far_away(head: np.ndarray, tail: np.ndarray) -> np.ndarray:
    distance = head - tail
    if max(abs(distance)) > 1:
        return distance
    return np.array([])


def main():
    input_lines = read_input_lines()
    tail, head = np.array([0, 0]), np.array([0, 0])
    moves = {'L': np.array([0, -1]), 'U': np.array([1, 0]),
             'R': np.array([0, 1]), 'D': np.array([-1, 0])}

    t_positions = {(0, 0)}
    for line in input_lines:
        direction, amount = line.split()
        amount = int(amount)
        for num in range(amount):
            head += moves[direction]
            if (move := check_far_away(head, tail)).size > 0:
                tail += move - moves[direction]
                t_positions.add((tail[0], tail[1]))

    print(f'{len(t_positions)=}')


if __name__ == '__main__':
    main()
