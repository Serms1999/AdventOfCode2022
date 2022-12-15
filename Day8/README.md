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



## --- Part Two ---

Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of **trees**.


To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)


The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large [eaves](https://en.wikipedia.org/wiki/Eaves) to keep it dry, so they wouldn't be able to see higher than the tree house anyway.


In the example above, consider the middle `5` in the second row:


<pre><code>30373
25<b>5</b>12
65332
33549
35390
</code></pre>


- Looking up, its view is not blocked; it can see **`1`** tree (of height `3`).
- Looking left, its view is blocked immediately; it can see only **`1`** tree (of height `5`, right next to it).
- Looking right, its view is not blocked; it can see **`2`** trees.
- Looking down, its view is blocked eventually; it can see **`2`** trees (one of height `3`, then the tree of height `5` that blocks its view).


A tree's **scenic score** is found by **multiplying together** its viewing distance in each of the four directions. For this tree, this is **`4`** (found by multiplying `1 * 1 * 2 * 2`).


However, you can do even better: consider the tree of height `5` in the middle of the fourth row:

<pre><code>30373
25512
65332
33<b>5</b>49
35390
</code></pre>

- Looking up, its view is blocked at **`2`** trees (by another tree with a height of `5`).
- Looking left, its view is not blocked; it can see **`2`** trees.
- Looking down, its view is also not blocked; it can see **`1`** tree.
- Looking right, its view is blocked at **`2`** trees (by a massive tree of height `9`).


This tree's scenic score is **`8`** (`2 * 2 * 1 * 2`); this is the ideal spot for the tree house.


Consider each tree on your map. **What is the highest scenic score possible for any tree?**

<details>
    <summary>Solution</summary>

I have followed a similar approach as before. I go through every direction adding 1 if I can see that tree from the current one, that is repeated for every direction. Next, I multiply all the distances

```python
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
```

Lastly, I find the maximum among all of them.

```python
scenic_scores = np.zeros(np.shape(grid), dtype=int)
for i in range(num_rows):
    for j in range(num_cols):
        scenic_scores[i][j] = get_scenic_score(i, j, grid)

print(f'{np.amax(np.amax(scenic_scores))=}')
```

The answer is: `345744`.

</details>

