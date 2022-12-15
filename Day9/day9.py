from IO.IO_module import read_input_lines
import numpy as np


def main():
    input_lines = read_input_lines(file_name='test_input')
    T, H = np.array([0, 0]), np.array([0, 0])
    moves = {'L': np.array([0, -1]), 'U': np.array([1, 0]),
             'R': np.array([0, 1]), 'D': np.array([-1, 0])}

    t_positions = {(0, 0)}
    previous_dir = ''
    positions = np.full((5, 6), '.', dtype=str)
    positions[0][0] = '#'
    for line in input_lines:
        direction, amount = line.split()
        amount = int(amount)
        H += moves[direction]
        for num in range(amount - 1):
            H += moves[direction]
            if H[0] != T[0] and H[1] != T[1] and max(abs(H[0]-T[0]), abs(H[1]-T[1])) > 1:
                T += moves[previous_dir]
            elif np.array_equal(H, T):
                previous_dir = direction
                continue

            if max(abs(H[0]-T[0]), abs(H[1]-T[1])) > 1:
                T += moves[direction]
                t_positions.add((T[0], T[1]))
            positions[T[0], T[1]] = '#'
            for _ in range(20):
                print()
            print(np.flip(positions, axis=0))
            print()

        previous_dir = direction

    print(f'{t_positions=}, {len(t_positions)=}')


if __name__ == '__main__':
    main()
