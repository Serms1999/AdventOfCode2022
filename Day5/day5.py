from IO.IO_module import read_input_lines
import re


def parse_lines(procedure: list) -> (list, list):
    index = procedure.index('')
    stack_lines, moves_lines = procedure[:index], procedure[index+1:]
    num_stack = max([int(x) for x in re.findall(r'([0-9]+)', stack_lines.pop())])
    stack_lines.reverse()

    stacks = [[] for _ in range(num_stack)]
    for line in stack_lines:
        crates = re.findall(pattern=r'(\[[A-Z]\]|\s\s\s)\s?', string=line)
        for index, crate in enumerate(crates):
            if crate != '   ':
                stacks[index].append(crate[1])

    moves = []
    pat = re.compile(pattern=r'move ([0-9]+) from ([0-9]+) to ([0-9]+)')
    for move in moves_lines:
        mat = re.match(pattern=pat, string=move)
        moves.append({'num': int(mat.group(1)), 'from': int(mat.group(2)) - 1, 'to': int(mat.group(3)) - 1})

    return stacks, moves


def move_crate(stack_from: list, stack_to: list, num_elem: int) -> None:
    crate_list = []
    for _ in range(num_elem):
        crate_list.append(stack_from.pop())
    crate_list.reverse()
    stack_to.extend(crate_list)


def main():
    input_lines = read_input_lines()
    stacks, moves = parse_lines(input_lines)

    for move in moves:
        move_crate(stacks[move['from']], stacks[move['to']], move['num'])

    top_crates = ''
    for stack in stacks:
        try:
            top_crates += stack.pop()
        except IndexError:
            # Empty stack
            pass

    print(f'{top_crates=}')


if __name__ == '__main__':
    main()
