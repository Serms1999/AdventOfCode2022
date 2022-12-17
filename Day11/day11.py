from IO.IO_module import read_input_lines
import numpy as np


def square(values: list) -> int:
    return values[0]**2


functions = {'square': square, 'add': sum, 'mult': np.prod}


def parse_monkeys(input_lines: list) -> list:
    ###############################################################
    # monkey: {'items': [item1, item2...],                        #
    #          'op': [op, arg],                                   #
    #          'test': [div, next_monkey_true, next_monkey_false]}#
    ###############################################################

    monkeys = []
    monkey_num = -1
    current_monkey = []
    for line in input_lines:
        if line == '':
            continue
        cmd, value = line.split(':')
        if 'Monkey' in cmd:
            monkey_num += 1
            monkeys.append({'items': [], 'op': [], 'test': []})
            current_monkey = monkeys[monkey_num]
        elif 'items' in cmd:
            current_monkey['items'] = [int(x) for x in value.split(',')]
        elif 'Operation' in cmd:
            _, op, arg2 = value.split(' = ')[1].split(' ')
            if 'old' == arg2:
                current_monkey['op'] = ['square']
            elif op == '+':
                current_monkey['op'] = ['add', int(arg2)]
            elif op == '*':
                current_monkey['op'] = ['mult', int(arg2)]
        elif 'Test' in cmd:
            current_monkey['test'].append(int(value.split('by ')[1]))
        elif 'true' in cmd or 'false' in cmd:
            current_monkey['test'].append(int(value.split('monkey ')[1]))

    return monkeys


def calculate_worry(monkey: dict, item: int) -> int:
    op, args = monkey['op'][0], [int(x) for x in monkey['op'][1:]]
    return functions[op](args + [item])


def main():
    input_lines = read_input_lines()
    monkeys = parse_monkeys(input_lines)
    monkey_inspections = np.zeros(len(monkeys), dtype=int)

    mods = np.prod([monkey['test'][0] for monkey in monkeys])

    for _ in range(10_000):
        for index, monkey in enumerate(monkeys):
            while len(monkey['items']):
                item = monkey['items'].pop(0)
                worry_level = calculate_worry(monkey, item)
                worry_level = worry_level % mods
                divisible = worry_level % monkey['test'][0] == 0
                next_monkey = monkey['test'][2 - int(divisible)]
                monkeys[next_monkey]['items'].append(worry_level)
                monkey_inspections[index] += 1

    monkey_business = np.prod(sorted(monkey_inspections, reverse=True)[0:2])
    print(f'{monkey_business=}')


if __name__ == '__main__':
    main()
