# ----------common for both parts
from collections import defaultdict

inp = [s.strip("\n") for s in open("input.txt")]
stones_inp = [int(x) for x in inp[0].split(" ")]
# ----------common for both parts

# ----------part 1
# The solution for part 1 is naive.
blinks = 25
stones = stones_inp.copy()
for _ in range(blinks):
    i = 0
    while i < len(stones):
        s = stones[i]
        _str = str(s)
        if s == 0:
            stones[i] = 1
        elif len(_str) % 2 == 0:
            m = len(_str) // 2
            a, b = int(_str[:m]), int(_str[m:])
            stones[i] = b
            stones.insert(i, a)
            i += 1
        else:
            stones[i] = s * 2024
        i += 1

answer1 = len(stones)

print(f"Part 1 answer: {answer1}")
# ----------part 1

# ----------part 2
# the solution for part 2 works with the stones in batches.
# How the stones change doesn't depend on anything but their own value.
# Therefore all stones with the same value will have the same outcome.
# And since we don't care about the ordering of the stones, and only the
# count of the stones, we can use a dictionary that keeps track
# of how many stones there are of each value.
blinks = 75
stones = {s: 1 for s in stones_inp}
for round in range(blinks):
    new_stones = defaultdict(int)
    for s, count in stones.items():
        _str = str(s)
        if s == 0:
            new_stones[1] += count
        elif len(_str) % 2 == 0:
            m = len(_str) // 2
            a, b = int(_str[:m]), int(_str[m:])
            new_stones[a] += count
            new_stones[b] += count
        else:
            new_stones[s * 2024] += count
    stones = new_stones.copy()

answer2 = sum(stones.values())

print(f"Part 2 answer: {answer2}")
# ----------part 2
