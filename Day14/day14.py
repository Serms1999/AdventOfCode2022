from IO.IO_module import read_input_lines


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


def get_possible_points(point: (int, int)) -> list:
    return [(point[0] + 1, point[1]),
            (point[0] + 1, point[1] - 1),
            (point[0] + 1, point[1] + 1)]


def blocked(cave: dict, point: (int, int), deepest: int) -> bool:
    if point[0] == deepest:
        return True
    return point[0] in cave and point[1] in cave[point[0]]


def main():
    input_lines = read_input_lines()
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


if __name__ == '__main__':
    main()
