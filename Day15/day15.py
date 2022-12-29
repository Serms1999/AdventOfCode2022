from IO.IO_module import read_input_lines
from copy import deepcopy
from time import time_ns
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
        aux_dict['lines'] = dict()
        aux_dict['lines']['tr'] = -1, sum(aux_dict['sensor']) + aux_dict['distance'] + 1
        aux_dict['lines']['tl'] = 1, aux_dict['sensor'][1] - aux_dict['sensor'][0] + aux_dict['distance'] + 1
        aux_dict['lines']['br'] = 1, aux_dict['sensor'][1] - aux_dict['sensor'][0] - aux_dict['distance'] - 1
        aux_dict['lines']['bl'] = -1, sum(aux_dict['sensor']) - aux_dict['distance'] - 1
        sensors.append(aux_dict)

    return sensors


def point_of_intersection(line1: (int, int), line2: (int, int)) -> (int, int):
    if line1[0] == line2[0]:
        return None
    x = (line1[1] - line2[1]) / 2
    y = (line1[1] + line2[1]) / 2
    if not x.is_integer() or not y.is_integer():
        return None
    if line1[0] == -1:
        return int(x), int(y)
    return int(-x), int(y)


def check_in_range(point: (int, int), minimum: int , maximum: int) -> bool:
    return minimum <= point[0] <= maximum and minimum <= point[1] <= maximum


def check_distance(sensors: list, point: (int, int)) -> bool:
    for sensor in sensors:
        if manhattan_distance(sensor['sensor'], point) <= sensor['distance']:
            return False

    return True


def main():
    input_lines = read_input_lines()
    start = time_ns()

    sensors = parse_sensors(input_lines)
    minimum, maximum = 0, 4_000_000
    possible_points = []
    for sensor in sensors:
        sensors_copy = deepcopy(sensors)
        sensors_copy.remove(sensor)
        for other in sensors_copy:
            lines1 = sensor['lines']
            lines2 = other['lines']
            for line1 in lines1.values():
                for line2 in lines2.values():
                    if point := point_of_intersection(line1, line2):
                        possible_points.append(point)

    possible_points = list(filter(lambda p: check_in_range(p, minimum, maximum), possible_points))

    for point in possible_points:
        if check_distance(sensors, point):
            break

    tuning_frequency = 4_000_000 * point[0] + point[1]
    exec_time = (time_ns() - start) / 1_000_000
    print(f'{point[0]=}, {point[1]=}, {tuning_frequency=}, {exec_time=}ms')


if __name__ == '__main__':
    main()
