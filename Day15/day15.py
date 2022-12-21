from IO.IO_module import read_input_lines
import re
import numpy as np


def manhattan_distance(p1: (int, int), p2: (int, int)) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse_sensors(area: list) -> (list, (int, int), (int, int)):
    sensors = []
    min_x, min_y = np.inf, np.inf
    max_x, max_y = -np.inf, -np.inf
    for line in area:
        aux_dict = dict()
        nums = re.findall(r'-?\d+', line)
        aux_dict['sensor'] = int(nums[0]), int(nums[1])
        aux_dict['beacon'] = int(nums[2]), int(nums[3])
        aux_dict['distance'] = manhattan_distance(aux_dict['sensor'], aux_dict['beacon'])
        sensors.append(aux_dict)

        min_x = min(min(aux_dict['sensor'][0], aux_dict['beacon'][0]), min_x)
        min_y = min(min(aux_dict['sensor'][1], aux_dict['beacon'][1]), min_y)
        max_x = max(max(aux_dict['sensor'][0], aux_dict['beacon'][0]), max_x)
        max_y = max(max(aux_dict['sensor'][1], aux_dict['beacon'][1]), max_y)

    return sensors, (min_x, min_y), (max_x, max_y)


def main():
    input_lines = read_input_lines(file_name='test_input')
    sensors, top_left, bottom_right = parse_sensors(input_lines)
    positions = np.full((bottom_right[1] - top_left[1], bottom_right[0] - top_left[0]), False, dtype=bool)

    for x in range(top_left[0], bottom_right[0]):
        for y in range(top_left[1], bottom_right[1]):
            for sensor in sensors[6:7]:
                if manhattan_distance((x, y), sensor['sensor']) <= sensor['distance']:
                    positions[y - top_left[1]][x - top_left[0]] = True
                    break

    for row in positions:
        for point in row:
            if point:
                print('#', end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    main()
