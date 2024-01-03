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
w, h = len(L[0]), len(L)

# ----------part 1
res = 0
vow = "aeiou"
for s in L:
    vow_c = 0
    doub = False
    bad = False
    for i, c in enumerate(s):
        if c in vow:
            vow_c += 1
        if i < len(s) - 1:
            if c == s[i + 1]:
                doub = True
            if s[i : i + 2] in ["ab", "cd", "pq", "xy"]:
                bad = True
                break
    if bad:
        continue
    if doub and vow_c >= 3:
        res += 1


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
res = 0
for s in L:
    rep = False
    doub = False
    D = {}
    for i, c in enumerate(s):
        if i < len(s) - 2 and c == s[i + 2]:
            rep = True
        if i < len(s) - 1:
            k = c + s[i + 1]
            if k in D:
                if i - D[k] >= 2:
                    doub = True
            else:
                D[k] = i

    if rep and doub:
        res += 1


print(f"Part 2 answer: {res}")
# ----------part 2
