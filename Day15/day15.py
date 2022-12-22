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


def main():
    input_lines = read_input_lines()
    sensors = parse_sensors(input_lines)
    row = 2_000_000

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

            try:
                if sensor_point[1] == row:
                    impossible_points.remove(sensor_point[0])
                if beacon_point[1] == row:
                    impossible_points.remove(beacon_point[0])
            except KeyError:
                pass

    print(f'{len(impossible_points)=}')


if __name__ == '__main__':
    main()
