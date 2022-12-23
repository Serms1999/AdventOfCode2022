from IO.IO_module import read_input_lines
import re


def manhattan_distance(p1: (int, int), p2: (int, int)) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_sensors(area: list) -> list:
    sensors = []
    for line in area:
        aux_dict = dict()
        nums = re.findall(r'-?\d+', line)
        aux_dict['sensor'] = int(nums[0]), int(nums[1])
        aux_dict['beacon'] = int(nums[2]), int(nums[3])
        aux_dict['distance'] = manhattan_distance(aux_dict['sensor'], aux_dict['beacon'])
        sensors.append(aux_dict)

    return sensors


def check_all_values(impossible_points: dict, y_index: int) -> bool:
    if y_index not in impossible_points:
        return True

    return not isinstance(impossible_points[y_index], range)


def update_impossible_points(impossible_points: dict, y_index: int, values: range, aux_range: range) -> None:
    aux_range_set = set(aux_range)
    if y_index not in impossible_points:
        impossible_points[y_index] = set(values)
    else:
        impossible_points[y_index].update(values)

    if impossible_points[y_index] == aux_range_set:
        impossible_points[y_index] = aux_range


def get_impossible_points(sensors: list, minimum: int, maximum: int) -> dict:
    impossible_points = dict()
    aux_range = range(minimum, maximum + 1)
    for sensor in sensors:
        sensor_point, _, distance = sensor.values()

        if check_all_values(impossible_points, sensor_point[1]) and minimum <= sensor_point[1] <= maximum:
            signal_range = range(sensor_point[0] - distance, sensor_point[0] + distance + 1)
            signal_range = set(filter(lambda s: minimum <= s <= maximum, signal_range))
            update_impossible_points(impossible_points, sensor_point[1], signal_range, aux_range)

        for x in range(1, distance + 1):
            if check_all_values(impossible_points, sensor_point[1] + x) and minimum <= sensor_point[1] + x <= maximum:
                signal_range = range(sensor_point[0] - distance, sensor_point[0] + distance + 1)[x:-x]
                signal_range = set(filter(lambda s: minimum <= s <= maximum, signal_range))
                update_impossible_points(impossible_points, sensor_point[1] + x, signal_range, aux_range)

            if not (check_all_values(impossible_points, sensor_point[1] - x) and minimum <= sensor_point[1] - x <= maximum):
                continue

            update_impossible_points(impossible_points, sensor_point[1] - x, signal_range, aux_range)

    return impossible_points


def remove_range(ranges: list, value: range) -> None:
    index = -1
    for idx, r in enumerate(ranges):
        if min(value) in r:
            index = idx
            break

    if index == -1:
        return

    r = ranges.pop(index)
    a, b = min(r), max(r)
    if low_range := range(a, min(value)):
        ranges.append(low_range)
    if high_range := range(max(value) + 1, b + 1):
        ranges.append(high_range)


def possible_points(sensors: list, all_possible: dict, range_possible: range) -> None:
    minimum, maximum = min(range_possible), max(range_possible)
    for sensor in sensors:
        sensor_point, _, distance = sensor.values()

        signal_range = range(sensor_point[0] - distance, sensor_point[0] + distance + 1)
        if minimum <= sensor_point[1] <= maximum:
            remove_range(all_possible[sensor_point[1]], filter(lambda s: minimum <= s <= maximum, signal_range))

        for x in range(1, distance + 1):
            if minimum <= sensor_point[1] + x <= maximum:
                remove_range(all_possible[sensor_point[1] + x], filter(lambda s: minimum <= s <= maximum, signal_range[x:-x]))

            if minimum <= sensor_point[1] - x <= maximum:
                remove_range(all_possible[sensor_point[1] - x], filter(lambda s: minimum <= s <= maximum, signal_range[x:-x]))


def print_sensors(impossible_points, all_possible):
    for y in all_possible:
        print(f'{y}\t', end='')
        if y not in impossible_points:
            print('.'*(all_possible[-1] + 1))
        elif isinstance(impossible_points[y], range):
            print('#'*(all_possible[-1] + 1))
        else:
            for x in all_possible:
                if x in impossible_points[y]:
                    print('#', end='')
                else:
                    print('.', end='')
            print()


def main():
    input_lines = read_input_lines(file_name='test_input')
    sensors = parse_sensors(input_lines)

    minimum, maximum = 0, 20
    range_possible = range(minimum, maximum + 1)
    all_possible = {x: [range_possible] for x in range_possible}
    possible_points(sensors, all_possible, range_possible)

    for i, v in all_possible.items():
        if v:
            print(f'{i=}, {v=}')


if __name__ == '__main__':
    main()
