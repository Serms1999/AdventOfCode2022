from IO.IO_module import read_input_lines
from functools import cache
import re

valves = dict()


def parse_valves(valves_str: list) -> dict:
    parsed_valves = dict()
    for valve_str in valves_str[0:]:
        valve, *tunnels = re.findall(pattern=r'[A-Z]{2}', string=valve_str)
        rate = int(re.search(pattern=r'\d+', string=valve_str).group(0))
        parsed_valves[valve] = {'rate': rate, 'tunnels': tunnels}

    return parsed_valves


@cache
def resolve_situation(cur_valve: str, opened: tuple, remaining_time: int, elephant: bool) -> int:
    if not remaining_time:
        if elephant:
            return resolve_situation('AA', opened, 26, False)
        return 0

    tunnels = valves[cur_valve]['tunnels']
    rate = valves[cur_valve]['rate']
    max_flow = max([resolve_situation(valve, opened, remaining_time - 1, elephant) for valve in tunnels])

    if rate and cur_valve not in opened:
        new_opened = set(opened)
        new_opened.add(cur_valve)
        max_flow = max(
            max_flow,
            (rate*(remaining_time-1)) + resolve_situation(cur_valve, tuple(new_opened), remaining_time - 1, elephant)
        )

    return max_flow


def main():
    global valves
    input_lines = read_input_lines()
    valves = parse_valves(input_lines)
    pressure_released = resolve_situation('AA', tuple(), remaining_time=26, elephant=True)
    print(f'{pressure_released=}')


if __name__ == '__main__':
    main()
