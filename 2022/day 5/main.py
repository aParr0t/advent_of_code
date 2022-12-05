# read input
inp = [s.rstrip("\n") for s in open("input.txt")]

# ----------both parts
stack_count = (len(inp[0]) - 3) // 4 + 1


def populate_stacks():
    stacks = [[] for _ in range(stack_count)]
    for row in inp[: inp.index("") - 1]:
        for i in range(0, stack_count):
            crate = row[1 + i * 4]
            if crate != " ":
                stacks[i].insert(0, crate)
    return stacks


instructions = []
for s in inp[inp.index("") + 1 :]:
    s = s.replace("move ", "").replace("from ", "").replace("to ", "")
    s = [int(x) for x in s.split(" ")]
    s[1] -= 1
    s[2] -= 1
    instructions.append(s)
# ----------both parts

# ----------part 1
stacks = populate_stacks()
for move_count, from_stack, to_stack in instructions:
    moved_crates = [stacks[from_stack].pop() for _ in range(move_count)]
    stacks[to_stack].extend(moved_crates)

stack_tops = [x[-1] for x in stacks]
print(f"Part 1 answer: {''.join(stack_tops)}")
# ----------part 1

# ----------part 2
stacks = populate_stacks()
for move_count, from_stack, to_stack in instructions:
    moved_crates = stacks[from_stack][-move_count:]
    del stacks[from_stack][-move_count:]
    stacks[to_stack].extend(moved_crates)

stack_tops = [x[-1] for x in stacks]
print(f"Part 2 answer: {''.join(stack_tops)}")
# ----------part 2
