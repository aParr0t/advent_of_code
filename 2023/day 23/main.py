import functools
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)

# ----------part 1
# part 1 was alright. Just messed up a few times when calculating the distances
inv = {
    (1, 0): "<",
    (-1, 0): ">",
    (0, 1): "^",
    (0, -1): "v",
}

M = defaultdict(lambda: defaultdict(lambda: 0))  # (x, y): {(x1, y1): 34, (x2, y2): 12}


def map_out(pos: tuple, dist: int, V: set, origin: tuple):
    x, y = pos
    while True:
        dist += 1
        P = []
        for dx, dy in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w) or not (0 <= ny < h):
                continue
            if G[ny][nx] == "#" or G[ny][nx] == inv[(dx, dy)]:
                continue
            if (nx, ny) in V:
                continue
            P.append((nx, ny))
        V.add((x, y))
        if len(P) == 1:
            x, y = P[0]
            continue
        else:
            M[origin][(x, y)] = max(dist, M[origin][(x, y)])
            for p in P:
                map_out(p, 0, deepcopy(V), (x, y))
            return


s = (1, 0)
map_out(s, -1, set(), s)

res = 0
Q = [((1, 0), 0)]
while Q:
    pos, d = Q.pop()
    if pos == (w - 2, h - 1):
        res = max(res, d)
        continue
    for n, nd in M[pos].items():
        Q.append((n, d + nd))


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# Slow algorithm, but it works! Apparently this is an NP problem?
M = defaultdict(lambda: defaultdict(lambda: 0))  # (x, y): {(x1, y1): 34, (x2, y2): 12}


def map_out(pos: tuple):
    x, y = pos
    D = {}
    Q = [(0, pos)]
    J = []
    while Q:
        d, (x, y) = heapq.heappop(Q)
        if (x, y) in D:
            continue
        D[(x, y)] = d

        P = []
        for dx, dy in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w) or not (0 <= ny < h):
                continue
            if G[ny][nx] == "#":
                continue
            if (nx, ny) in D:
                continue
            P.append((d + 1, (nx, ny)))
        if len(P) == 1 or (x, y) == pos:
            Q.extend(P)
        else:
            M[pos][(x, y)] = d
            J.append((x, y))
    return J


# map out the distances and connections between the junctions
Q = [(1, 0)]
while Q:
    c = Q.pop()
    if c in M:
        continue
    J = map_out(c)
    for j in J:
        Q.append(j)

# find longest path
res = 0
Q = [((1, 0), 0, set())]
while Q:
    pos, d, V = Q.pop()
    V.add(pos)
    if pos == (w - 2, h - 1):
        res = max(res, d)
        continue
    for n, nd in M[pos].items():
        if n in V:
            continue
        Q.append((n, d + nd, set(V)))


print(f"Part 2 answer: {res}")
# ----------part 2
