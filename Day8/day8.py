from IO.IO_module import read_input_lines
import numpy as np


def parse_forest(input_lines: list) -> np.ndarray:
    forest = []
    for line in input_lines:
        forest.append([int(x) for x in list(line)])

    return np.array(forest)


def check_tree_visibility(x: int, y: int, grid: np.ndarray) -> bool:
    num_rows, num_cols = np.shape(grid)

    value = grid[x][y]
    grid_transpose = np.transpose(grid)
    current_row = grid[x]
    current_col = grid_transpose[y]

    if all(map(lambda t: t < value, current_row[0:y])):
        # Left visibility
        return True
    if all(map(lambda t: t < value, current_col[0:x])):
        # Top visibility
        return True
    if all(map(lambda t: t < value, current_row[y+1:num_cols])):
        # Right visibility
        return True
    if all(map(lambda t: t < value, current_col[x+1:num_rows])):
        # Bottom visibility
        return True
    # Not visible
    return False


def main():
    input_lines = read_input_lines(root_file=__file__)
    grid = parse_forest(input_lines)
    num_rows, num_cols = np.shape(grid)

    visible_trees = 2*num_rows + 2*(num_cols - 2)
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            visible_trees += check_tree_visibility(i, j, grid)

    print(f'{visible_trees=}')


if __name__ == '__main__':
    main()
