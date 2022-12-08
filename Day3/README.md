# Day 3: Rucksack Reorganization

## Part 1


One Elf has the important job of loading all of the [rucksacks](https://en.wikipedia.org/wiki/Rucksack) with supplies
for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now 
need to be rearranged.

Each rucksack has two large **compartments**. All items of a given type are meant to go into exactly one of the two
compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help 
finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, `a` and `A` refer
to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same
number of items in each of its two compartments, so the first half of the characters represent items in the first
compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

```
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

- The first rucksack contains the items `vJrwpWtwJgWrhcsFMMfFFhFp`, which means its first compartment contains the 
items `vJrwpWtwJgWr`, while the second compartment contains the items `hcsFMMfFFhFp`. The only item type that appears
in both compartments is lowercase `p`.
- The second rucksack's compartments contain `jqHRNqRjqzjGDLGL` and `rsFMfFZSrLrFZsSL`. The only item type that appears
in both compartments is uppercase `L`.
- The third rucksack's compartments contain `PmmdzqPrV` and `vPwwTWBwg`; the only common item type is uppercase `P`.
- The fourth rucksack's compartments only share item type `v`.
- The fifth rucksack's compartments only share item type `t`.
- The sixth rucksack's compartments only share item type `s`.

To help prioritize item rearrangement, every item type can be converted to a **priority**:
Lowercase item types `a` through `z` have priorities 1 through 26.
Uppercase item types `A` through `Z` have priorities 27 through 52.

In the above example, the priority of the item type that appears in both compartments of each rucksack is
16 (`p`), 38 (`L`), 42 (`P`), 22 (`v`), 20 (`t`), and 19 (`s`); the sum of these is **`157`**.

Find the item type that appears in both compartments of each rucksack. **What is the sum of the priorities of those 
item types?**

<details>
    <summary>Solution</summary>

First of all, we have to split the rucksack into its compartments. We can use sets because we are dealing with type of
objects, not objects.

```python
def get_compartments(input_lines: list) -> list:
    compartments = []
    for line in input_lines:
        half_length = len(line) // 2
        half1, half2 = line[:half_length], line[half_length:]
        compartments.append((set(half1), set(half2)))

    return compartments
```

Secondly, it's necessary to get the common object. Since we are using sets we can easily accomplish that 
using set intersection.

```python
def get_repeated_items(compartments: list) -> list:
    repeated_items = []
    for half1, half2 in compartments:
        common_item = half1.intersection(half2).pop()
        repeated_items.append(common_item)

    return repeated_items
```

Lastly, we can simply map each item with its priority using a lambda function.
```python
sum(map(lambda i: calculate_priority(i), repeated_items))
```

To calculate each priority, I use character ordinals.
```python
def calculate_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27
```

The answer is: `7821`.
</details>