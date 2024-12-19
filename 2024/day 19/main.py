# ----------common for both parts
from collections import defaultdict
from functools import lru_cache

inp = [s.strip("\n") for s in open("input.txt")]
towels = inp[0].split(", ")
patterns = inp[2:]

start = defaultdict(list)
for t in towels:
    start[t[0]].append(t)
# ----------common for both parts


# ----------part 1
@lru_cache
def search(s, idx=0):
    if idx >= len(s):
        return True
    start_c = s[idx]
    for towel in start[start_c]:
        if s[idx : idx + len(towel)] == towel:
            if search(s, idx + len(towel)):
                return True
    return False


total = 0
for i, pattern in enumerate(patterns):
    if search(pattern):
        total += 1

print(f"Part 1 answer: {total}")
# ----------part 1


# ----------part 2
@lru_cache
def ways(s, idx=0):
    if idx >= len(s):
        return 1
    start_c = s[idx]
    total = 0
    for towel in start[start_c]:
        if s[idx : idx + len(towel)] == towel:
            total += ways(s, idx + len(towel))
    return total


answer2 = 0
for pattern in patterns:
    answer2 += ways(pattern)

print(f"Part 2 answer: {answer2}")
# ----------part 2
