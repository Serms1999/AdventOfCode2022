from IO.IO_module import read_input_lines
import re


def parse_lines(procedure: list) -> (list, list):
    index = procedure.index('')
    stack_lines, moves_lines = procedure[:index], procedure[index+1:]
    num_stack = max([int(x) for x in re.findall(r'([0-9]+)', stack_lines.pop())])
    stack_lines.reverse()

    stacks = [[]] * num_stack
    pat = re.compile(pattern=r'(\[[A-Z]\]|   )[ (\[[A-Z]\]|   )]{2}')
    mat = pat.match(stack_lines[0])
    print(f'{mat.group(1)=}, {mat.group(2)=}, {mat.group(3)=}')


    return '', ''


def move_crate(stack_from: list, stack_to: list, num_elem: int) -> None:
    for _ in range(num_elem):
        elem = stack_from.pop()
        stack_to.append(elem)


def main():
    input_lines = read_input_lines(root_file=__file__, file_name='test_input')
    stacks, moves = parse_lines(input_lines)


if __name__ == '__main__':
    main()
