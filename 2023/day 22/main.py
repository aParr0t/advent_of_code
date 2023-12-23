import functools
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)


class Block:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.id = None

    def __iter__(self):
        return iter([self.x, self.y, self.z])


class Brick:
    _id = 65

    def __init__(self, bl: list[Block]):
        self.bl = bl
        self.id = chr(Brick._id)
        Brick._id += 1
        for b in self.bl:
            b.id = self.id

    def __getitem__(self, item):
        return self.bl[item]


# initialize bricks
B: list[Brick] = []
for l in L:
    ar = l.split("~")
    s, e = [[int(x) for x in a.split(",")] for a in ar]
    if s[2] > e[2]:
        s, e = e, s
    b = []
    for x in range(s[0], e[0] + 1):
        for y in range(s[1], e[1] + 1):
            for z in range(s[2], e[2] + 1):
                b.append(Block(x, y, z))
    B.append(Brick(b))

# bounding box
w = max([max(bl.x for bl in b) for b in B]) + 1
l = max([max(bl.y for bl in b) for b in B]) + 1
h = max([max(bl.z for bl in b) for b in B]) + 1

# sort for more optimal simulation
B.sort(key=lambda b: b[0].z)

# create grid
G = [[[0 for x in range(w)] for y in range(l)] for z in range(h)]
for b in B:
    for bl in b.bl:
        G[bl.z][bl.y][bl.x] = bl

# run the simulation
while True:
    moved = False
    for b in B:
        sz = b.bl[0].z
        nz = sz
        try:
            while nz > 1:
                nz -= 1
                for x, y, _ in b.bl:
                    g = G[nz][y][x]
                    if g != 0 and g not in b.bl:
                        nz = nz + 1
                        raise "can't move any further"
        except:
            pass

        if nz == sz:
            continue  # block can't move
        moved = True  # block can move
        # remove blocks from grid
        for bl in b.bl:
            G[bl.z][bl.y][bl.x] = 0
        # update grid
        for bl in b.bl:
            dz = nz - sz
            bl.z += dz
            G[bl.z][bl.y][bl.x] = bl

    if not moved:
        break


# find number of bricks that each brick is supporting and resting upon
O = defaultdict(set)
U = defaultdict(set)
for b in B:
    for bl in b:
        g = G[bl.z + 1][bl.y][bl.x]
        if isinstance(g, Block) and g not in b.bl:
            O[b.id].add(g.id)
            U[g.id].add(b.id)

# ----------part 1
# a brick can be disintegrated only if it has no bricks on top of it, or if
# the bricks above it are supported by multiple bricks
A = set()
for b in B:
    if len(O[b.id]) == 0:
        A.add(b.id)
        continue
    if all([len(U[o]) >= 2 for o in O[b.id]]):
        A.add(b.id)
        continue


res = len(A)

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# I avoided simulating all the bricks by just using the previous support-data.
# For each brick, start by marking it as "fallen". Then for each brick resting
# on it, check if it would fall. Repeat recursively or with a stack.
res = 0
for b in B:
    Q = list(O[b.id])
    fallen = set(b.id)
    while Q:
        b1 = Q.pop(0)
        rem = U[b1].difference(fallen)
        if len(rem) == 0:
            Q.extend(list(O[b1]))
            fallen.add(b1)
    res += len(fallen) - 1


print(f"Part 2 answer: {res}")
# ----------part 2
