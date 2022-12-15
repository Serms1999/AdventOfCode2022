## --- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a [tree house](https://en.wikipedia.org/wiki/Tree_house).


First, determine whether there is enough tree cover here to keep a tree house **hidden**. To do this, you need to count the number of trees that are **visible from outside the grid** when looking directly along a row or column.


The Elves have already launched a [quadcopter](https://en.wikipedia.org/wiki/Quadcopter) to generate a map with the height of each tree (your puzzle input). For example:



```
30373
25512
65332
33549
35390
```

Each tree is represented as a single digit whose value is its height, where `0` is the shortest and `9` is the tallest.


A tree is **visible** if all of the other trees between it and an edge of the grid are **shorter** than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.


All of the trees around the edge of the grid are **visible** - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the **interior nine trees** to consider:


- The top-left `5` is **visible** from the left and top. (It isn't visible from the right or bottom since other trees of height `5` are in the way.)
- The top-middle `5` is **visible** from the top and right.
- The top-right `1` is not visible from any direction; for it to be visible, there would need to only be trees of height **0** between it and an edge.
- The left-middle `5` is **visible**, but only from the right.
- The center `3` is not visible from any direction; for it to be visible, there would need to be only trees of at most height `2` between it and an edge.
- The right-middle `3` is **visible** from the right.
- In the bottom row, the middle `5` is **visible**, but the `3` and `4` are not.


With 16 trees visible on the edge and another 5 visible in the interior, a total of **`21`** trees are visible in this arrangement.


Consider your map; **how many trees are visible from outside the grid?**


<details>
    <summary>Solution</summary>

First of all, I parse the forest as matrix.

```python
def parse_forest(input_lines: list) -> np.ndarray:
    forest = []
    for line in input_lines:
        forest.append([int(x) for x in list(line)])

    return np.array(forest)
```

To check if a tree is visible, I use the transpose matrix to obtain the vertical axis as a normal list. After that, I divide the list y two, the elements before and after the tree (in the vertical axis this corresponds to the trees above or below the tree).
Lastly, I check if all the trees in each of the sublist is smaller than the current tree.

```python
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
```

The answer is: `1533`.

</details>



