## --- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked **crates**, but because the needed supplies are buried under many other crates, the crates need to be rearranged.


The ship has a **giant cargo crane** capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.


The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her **which** crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.


They do, however, have a drawing of the starting stacks of crates **and** the rearrangement procedure (your puzzle input). For example:



```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```

In this example, there are three stacks of crates. Stack 1 contains two crates: crate `Z` is on the bottom, and crate `N` is on top. Stack 2 contains three crates; from bottom to top, they are crates `M`, `C`, and `D`. Finally, stack 3 contains a single crate, `P`.


Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:



```
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
```

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved **one at a time**, so the first crate to be moved (`D`) ends up below the second and third crates:



```
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
```

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved **one at a time**, crate `C` ends up below crate `M`:



```
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
```

Finally, one crate is moved from stack 1 to stack 2:



<pre><code>      
        [<b>Z</b>]
        [N]
        [D]
[<b>C</b>] [<b>M</b>] [P]
 1   2   3
</code></pre>

The Elves just need to know **which crate will end up on top of each stack**; in this example, the top crates are `C` in stack 1, `M` in stack 2, and `Z` in stack 3, so you should combine these together and give the Elves the message **`CMZ`**.


**After the rearrangement procedure completes, what crate ends up on top of each stack?**

<details>
    <summary>Solution</summary>

First of all, it is necessary to parse the input. The stacks will be parsed as a list of heaps. On the other hand, the moves will be parsed as tuples such as (_from_, _to_, _num_). To achieve this result, I used regular expressions.

The parse function is the following:

```python
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
```

Once we have this representation, it is so simple to move elements from one stack to another.

```python
def move_crate(stack_from: list, stack_to: list, num_elem: int) -> None:
    for _ in range(num_elem):
        elem = stack_from.pop()
        stack_to.append(elem)

        
for move in moves:
    move_crate(stacks[move['from']], stacks[move['to']], move['num'])
```

Lastly, we need to get the top element from each stack.

```python
top_crates = ''
    for stack in stacks:
        try:
            top_crates += stack.pop()
        except IndexError:
            # Empty stack
            pass
```

</details>
