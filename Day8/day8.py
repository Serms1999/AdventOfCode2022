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


def get_scenic_score(x: int, y: int, grid: np.ndarray) -> int:
    num_rows, num_cols = np.shape(grid)

    def get_view(trees: np.ndarray) -> int:
        score = 0
        for tree in trees:
            if tree >= value:
                score += 1
                break
            score += 1
        return score

    value = grid[x][y]
    grid_transpose = np.transpose(grid)
    current_row = grid[x]
    current_col = grid_transpose[y]

    left_trees, right_trees = np.flip(current_row[0:y]), current_row[y+1:num_cols]
    up_trees, down_trees = np.flip(current_col[0:x]), current_col[x+1:num_rows]

    left = get_view(left_trees)
    up = get_view(up_trees)
    right = get_view(right_trees)
    down = get_view(down_trees)

    return left * up * right * down


def main():
    input_lines = read_input_lines()
    grid = parse_forest(input_lines)
    num_rows, num_cols = np.shape(grid)

    scenic_scores = np.zeros(np.shape(grid), dtype=int)
    for i in range(num_rows):
        for j in range(num_cols):
            scenic_scores[i][j] = get_scenic_score(i, j, grid)

    print(f'{np.amax(np.amax(scenic_scores))=}')


if __name__ == '__main__':
    main()
