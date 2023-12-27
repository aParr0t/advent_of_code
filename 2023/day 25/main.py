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
b, h = len(L[0]), len(L)

# ----------part 1
# Pretty difficult. I actually gave up once and began reading the AOC subreddit.
# But then I read one guy being super happy about finding a solution by
# himself and I stopped immediately. So I came up with this algorithm. It is
# inspired by Karger's algorithm in the sense that it uses randomness. I found
# Karger's algorithm when searching for an algorithm specifically for solving
# the global min-cut problem.
# My algorithm works by:
#   1. approximating the diameter of the graph
#   2. Finding the "hottest" nodes of the graph by repeating very many times:
#       picking two random nodes -> if their distance is near the diameter,
#       then add the nodes of the path to a counter. The nodes of the path are
#       counted unequally; they have different weights.
#       Nodes near the ends of the path are weighted less than the nodes in the
#       middle. This is because the three bridges of the graph have a higher
#       probability of being near the middle. I think this weighing was pretty
#       smart of me :)
#   3. From the possible edges between the "hottest" nodes, try every
#       trio. Check if the trio is the correct by first removing the edges from
#       the graph. Then count the number of reachable nodes from one of the
#       vertices. If the number of reachable nodes is less than the total
#       number of nodes, then the graph must have been cut in two.
C = defaultdict(set)
for l in L:
    r, con = l.split(": ")
    con = con.split(" ")
    for c in con:
        C[r].add(c)
        C[c].add(r)

C = {k: list(v) for k, v in C.items()}
K = list(C.keys())


# approximate the diameter of the graph
mx_dist = 0
for i in range(10):
    a = random.choice(K)
    Q = [a]
    D = {}
    d = 0
    while Q:
        NQ = []
        while Q:
            c = Q.pop(0)
            if c in D:
                continue
            D[c] = d
            for o in C[c]:
                if o in D:
                    continue
                NQ.append(o)
        d += 1
        Q = NQ
    mx_dist = max(*D.values(), mx_dist)


# function for finding path between two nodes in the graph
def find(a, b, M):
    Q = [a]
    prev = {}
    V = set([a])
    while Q:
        NQ = set()
        while Q:
            c = Q.pop()
            if c == b:
                NQ = []
                break
            for o in M[c]:
                if o in V:
                    continue
                V.add(o)
                NQ.add(o)
                prev[o] = c
        Q = list(NQ)

    path = []
    c = b
    while c in prev:
        path.append(c)
        c = prev[c]
    return path


# the algorithm is based on randomness, so repeat the process until an answer
# is found
res = None
while not res:
    # find the hottest nodes in the graph
    counter = Counter()
    md = int(mx_dist / 2)
    thr = int(mx_dist * 0.8)
    for _ in range(len(C)):
        a, b = random.choice(K), random.choice(K)
        if a == b:
            continue
        p = find(a, b, C)
        if len(p) < thr:
            continue
        # weigh the nodes unequally. Nodes near the center of the path should
        # be counted more importantly
        for i, c in enumerate(p):
            counter[c] += max(md - (abs(md - i)), 1)

    # find the possible edges between the "hottest" nodes
    R = []
    cmn = counter.most_common()[:10]
    E = set()
    KK = [k for k, r in cmn]
    for k in KK:
        for o in C[k]:
            if o not in KK:
                continue
            t = tuple(sorted([k, o]))
            E.add(t)

    # try every trio of possible edges. Remove the edges, then check if the
    # graph is cut in two.
    for es in itertools.combinations(E, 3):
        _C = deepcopy(C)
        for a, b in es:
            _C[a].remove(b)
            _C[b].remove(a)

        Q = [es[0][0]]
        V = set()
        while Q:
            c = Q.pop()
            for o in _C[c]:
                if o in V:
                    continue
                V.add(o)
                Q.append(o)
        if len(V) != len(C):
            # print("found the three edges to cut:")
            # print(es)
            s1 = len(V)
            s2 = len(C) - s1
            res = s1 * s2
            break


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# I pushed the BIG red button!
# ----------part 2
