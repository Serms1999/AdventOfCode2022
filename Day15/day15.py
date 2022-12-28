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
    minimum, maximum = 0, 4_000_000

    for row in range(maximum):
        impossible_points = set()
        for sensor in sensors:
            sensor_point, beacon_point, distance = sensor.values()
            if (offset := abs(row - sensor_point[1])) <= distance:
                signal_range = range(sensor_point[0] - distance, sensor_point[0] + distance + 1)
                if offset == 0:
                    impossible_points.update(signal_range)
                else:
                    if sensor_point[1] + offset == row:
                        impossible_points.update(signal_range[offset:-offset])
                    elif sensor_point[1] - offset == row:
                        impossible_points.update(signal_range[offset:-offset])

        aux_list = list(filter(lambda x: minimum <= x <= maximum, impossible_points))
        if len(aux_list) < maximum - minimum + 1:
            break

    x_coord = (set(range(minimum, maximum + 1)) - impossible_points).pop()
    tuning_frequency = 4_000_000 * x_coord + row
    print(f'{x_coord=}, {row=}, {tuning_frequency=}')


if __name__ == '__main__':
    main()
