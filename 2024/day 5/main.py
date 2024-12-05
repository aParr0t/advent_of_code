# ----------common for both parts
from collections import defaultdict
from functools import cmp_to_key

inp = [s.strip("\n") for s in open("input.txt")]
orderings_inp = inp[: inp.index("")]
updates_inp = inp[inp.index("") + 1 :]

# dependencies[a] = [b, c, d]    this means a depends on b, c and d
# aka. a should come after b, c and d
dependencies = defaultdict(list)
for up in orderings_inp:
    parent, child = map(int, up.split("|"))
    dependencies[child].append(parent)

# list of lists of int
# updates[i] = [29, 75, 13, ...]
updates = [list(map(int, s.split(","))) for s in updates_inp]
# ----------common for both parts


# ----------part 1 and 2
def compare(a: int, b: int):
    """
    Used for sorting the incorrect updates.
    This function compares two numbers a and b, and says
    which one should go before the other.

    The meaning of the return values:
    -1 == a should come before b
    0 == don't care
    1 == b should come before a
    """
    if a in dependencies[b]:
        # b depends on a
        return -1
    if b in dependencies[a]:
        # a depends on b
        return 1
    return 0


correct_total = incorrect_total = 0
for update in updates:
    seen = set()  # all the values checked in the current update
    for x in update:
        seen.add(x)
        # get all the dependencies while ignoring those that don't show up in the update
        parents = [p for p in dependencies[x] if p in update]
        if len(parents) == 0:
            # if no dependencies, go on
            continue
        if not all([p in seen for p in parents]):
            # fix the incorrect update
            up = update.copy()
            up.sort(key=cmp_to_key(compare))
            mid = up[len(up) // 2]
            incorrect_total += mid
            break
    else:
        mid = update[len(update) // 2]
        correct_total += mid

print(f"Part 1 answer: {correct_total}")
print(f"Part 2 answer: {incorrect_total}")
# ----------part 1 and 2
