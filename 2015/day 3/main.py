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

l = L[0]
# ----------part 1
V = set()
x, y = 0, 0
V.add((x, y))
for c in l:
    if c == ">":
        x += 1
    elif c == "^":
        y -= 1
    elif c == "<":
        x -= 1
    elif c == "v":
        y += 1
    V.add((x, y))

res = len(V)

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
V = set()
x = y = 0
x1 = y1 = 0
V.add((x, y))

for i, c in enumerate(l):
    dx = dy = 0
    if c == ">":
        dx += 1
    elif c == "^":
        dy -= 1
    elif c == "<":
        dx -= 1
    elif c == "v":
        dy += 1
    if i % 2 == 0:
        x += dx
        y += dy
    else:
        x1 += dx
        y1 += dy
    V.add((x, y))
    V.add((x1, y1))


res = len(V)

print(f"Part 2 answer: {res}")
# ----------part 2
