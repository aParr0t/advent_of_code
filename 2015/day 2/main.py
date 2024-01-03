import functools
import heapq
import itertools
import math
import random
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)

# ----------part 1
res = 0
for _l in L:
    l, w, h = [int(x) for x in _l.split("x")]
    x, y, z = l * w, w * h, h * l
    a = 2 * x + 2 * y + 2 * z
    a += min(x, y, z)
    res += a

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
res = 0
for _l in L:
    l, w, h = [int(x) for x in _l.split("x")]
    r = 2 * (l + w + h - max(l, w, h))
    r += l * w * h
    res += r

print(f"Part 2 answer: {res}")
# ----------part 2
