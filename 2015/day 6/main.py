import functools
import hashlib
import heapq
import itertools
import math
import random
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = 1000, 1000

I = []
for l in L:
    # parse input
    sp = l.split(" ")
    if "toggle" in l:
        c = sp[0]
    else:
        c = sp[0] + " " + sp[1]
    x1, y1 = [int(x) for x in sp[-3].split(",")]
    x2, y2 = [int(x) for x in sp[-1].split(",")]
    I.append((c, x1, y1, x2, y2))


# ----------part 1
G = [[False for _ in range(1000)] for _ in range(1000)]
for c, x1, y1, x2, y2 in I:
    # do the flipping
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if c == "turn on":
                G[i][j] = True
            elif c == "turn off":
                G[i][j] = False
            else:
                G[i][j] = not G[i][j]

res = 0
for i in range(w):
    for j in range(h):
        if G[i][j]:
            res += 1

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
G = [[0 for _ in range(1000)] for _ in range(1000)]
for c, x1, y1, x2, y2 in I:
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if c == "turn on":
                G[i][j] += 1
            elif c == "turn off":
                G[i][j] = max(0, G[i][j] - 1)
            else:
                G[i][j] += 2

res = 0
for i in range(w):
    for j in range(h):
        res += G[i][j]


print(f"Part 2 answer: {res}")
# ----------part 2
