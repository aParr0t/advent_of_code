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
u, d = l.count("("), l.count(")")
res = u - d

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
p = 0
for i, c in enumerate(l):
    if c == "(":
        p += 1
    else:
        p -= 1
    if p == -1:
        break

res = i + 1

print(f"Part 2 answer: {res}")
# ----------part 2
