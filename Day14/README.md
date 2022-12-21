## --- Day 14: Regolith Reservoir ---

The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads **behind** the waterfall.


Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.


As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!


Fortunately, your [familiarity](https://adventofcode.com/2018/day/17) with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly **air** with structures made of **rock**.


Your scan traces the path of each solid rock structure and reports the `x,y` coordinates that form the shape of the path, where `x` represents distance to the right and `y` represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:



```
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
```

This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from `498,4` through `498,6` and another line of rock from `498,6` through `496,6`.)


The sand is pouring into the cave from point `500,0`.


Drawing rock as `#`, air as `.`, and the source of the sand as `+`, this becomes:



```

  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
```

Sand is produced **one unit at a time**, and the next unit of sand is not produced until the previous unit of sand **comes to rest**. A unit of sand is large enough to fill one tile of air in your scan.


A unit of sand always falls **down one step** if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally **one step down and to the left**. If that tile is blocked, the unit of sand attempts to instead move diagonally **one step down and to the right**. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand **comes to rest** and no longer moves, at which point the next unit of sand is created back at the source.


So, drawing sand that has come to rest as `o`, the first unit of sand simply falls straight down and then stops:

<pre><code>......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......<b>o</b>.#.
#########.
</code></pre>

The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:



```
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
```

After a total of five units of sand have come to rest, they form this pattern:



```
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
```

After a total of 22 units of sand:



```
......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
```

Finally, only two more units of sand can possibly come to rest:

<pre><code>......+...
..........
......o...
.....ooo..
....#ooo##
...<b>o</b>#ooo#.
..###ooo#.
....oooo#.
.<b>o</b>.ooooo#.
#########.
</code></pre>

Once all **`24`** units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with `~`:



```
.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
```

Using your scan, simulate the falling sand. **How many units of sand come to rest before sand starts flowing into the abyss below?**


<details>
    <summary>Solution</summary>

To represent the cave, I use a dictionary with all the blocked points.

```python
def parse_point(point_str: str) -> (int, int):
    coordinates = point_str.split(',')
    return int(coordinates[0]), int(coordinates[1])


def parse_path(path_str: str) -> list:
    points = path_str.split(' -> ')
    return [parse_point(point) for point in points]


def get_range(item1: int, item2: int) -> range:
    min_value, max_value = min(item1, item2), max(item1, item2)
    return range(min_value, max_value + 1)


def add_point(cave: dict, x: int, y: int) -> None:
    if y not in cave:
        cave[y] = {x}
    else:
        cave[y].add(x)


def parse_cave(scan: list) -> dict:
    cave = {}
    for path in scan:
        points = parse_path(path)
        prev_point = points.pop(0)
        add_point(cave, prev_point[0], prev_point[1])
        while points:
            cur_point = points.pop(0)
            if prev_point[1] - cur_point[1] == 0:
                for x_range in get_range(prev_point[0], cur_point[0]):
                    add_point(cave, x_range, cur_point[1])
            else:
                for y_range in get_range(prev_point[1], cur_point[1]):
                    add_point(cave, cur_point[0], y_range)

            prev_point = cur_point

    return cave
```

Once the cave is parsed, the problem is simple: check if the sand could go further or not. If one unit of sand is as deep as the deepest point in the cave, it means that it will continue falling down.

```python
def get_possible_points(point: (int, int)) -> list:
    return [(point[0] + 1, point[1]),
            (point[0] + 1, point[1] - 1),
            (point[0] + 1, point[1] + 1)]


def blocked(cave: dict, point: (int, int)) -> bool:
    return point[0] in cave and point[1] in cave[point[0]]


cave = parse_cave(input_lines)

sand_units = 0
sand_falling = False
while not sand_falling:
    point = (0, 500)
    blocked_point = False
    while not blocked_point:
        if point[0] + 1 > max(cave.keys()):
            # Sand falls over
            sand_falling = True
            break

        options = [False, False, False]
        for index, possible_point in enumerate(get_possible_points(point)):
            if not blocked(cave, possible_point):
                point = possible_point
                options[index] = True
                break

        if not any(options):
            blocked_point = True
            add_point(cave, point[1], point[0])
            sand_units += 1

print(f'{sand_units=}')
```

The answer is: `618`.

</details>


## --- Part Two ---

You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!


You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a `y` coordinate equal to **two plus the highest `y` coordinate** of any point in your scan.


In the example above, the highest `y` coordinate of any point is `9`, and so the floor is at `y=11`. (This is as if your scan contained one extra rock path like `-infinity,11 -> infinity,11`.) With the added floor, the example above now looks like this:



```
        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
```

To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at `500,0`, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after **`93`** units of sand come to rest:



```
............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
```

Using your scan, simulate the falling sand until the source of the sand becomes blocked. **How many units of sand come to rest?**

<details>
    <summary>Solution</summary>

With the previous solution, I only have to do a few changes. Instead of checking if one unit of sand is falling over, I check if the initial point is already taken. This check is now done outside the inner loop.

```python
cave = parse_cave(input_lines)

sand_units = 0
deepest = max(cave) + 2
while True:
    if 0 in cave and 500 in cave[0]:
        break

    point = (0, 500)
    blocked_point = False
    while not blocked_point:
        options = [False, False, False]
        for index, possible_point in enumerate(get_possible_points(point)):
            if not blocked(cave, possible_point, deepest):
                point = possible_point
                options[index] = True
                break

        if not any(options):
            blocked_point = True
            add_point(cave, point[1], point[0])
            sand_units += 1

print(f'{sand_units=}')
```

In addition, to check the new floor I change the `blocked` function.

```python
def blocked(cave: dict, point: (int, int), deepest: int) -> bool:
    if point[0] == deepest:
        return True
    return point[0] in cave and point[1] in cave[point[0]]
```

The answer is: `26358`.

</details>
