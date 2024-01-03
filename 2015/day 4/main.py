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

l = L[0]


# ----------part 1
def find(pre: str, z_count: int):
    z = "0" * z_count
    i = 0
    while True:
        s = (pre + str(i)).encode()
        hsh = hashlib.md5(s)
        hx = hsh.hexdigest()
        if hx.startswith(z):
            break
        i += 1
    return i


res = find(l, 5)
print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# this one takes some time
res = find(l, 6)

print(f"Part 2 answer: {res}")
# ----------part 2
