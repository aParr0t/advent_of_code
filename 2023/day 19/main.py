import functools
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)

W = {}
for l in L[: L.index("")]:
    name, rs = l.split("{")
    R = []
    rs = rs[:-1].split(",")
    for i, r in enumerate(rs):
        if i == len(rs) - 1:
            R.append(r)
            continue
        c, e = r[2:].split(":")
        c = int(c)
        R.append([r[0], r[1], c, e])
    W[name] = R


# ----------part 1
# Part 1 was easy. Straightforward calculations based on rules.

P = []
for l in L[L.index("") + 1 :]:
    l = l[1:-1]
    p = {}
    for s in l.split(","):
        p[s[:1]] = int(s[2:])
    P.append(p)

A = []
for p in P:
    rs = W["in"]
    while rs:
        for r in rs[:-1]:
            cond = False
            if r[1] == "<" and p[r[0]] < r[2]:
                cond = True
            elif r[1] == ">" and p[r[0]] > r[2]:
                cond = True
            if cond:
                if r[-1] == "R":
                    rs = None
                    break
                if r[-1] == "A":
                    A.append(p)
                    rs = None
                    break
                else:
                    rs = W[r[-1]]
                    break
        else:
            if rs[-1] == "A":
                A.append(p)
                rs = None
            elif rs[-1] == "R":
                rs = None
            else:
                rs = W[rs[-1]]

res = 0
for a in A:
    res += sum(a.values())

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# I flashed part 2, proud of myself. A bit tricky part 2 though. The code works
# by starting with all combinations being possible. Then starting at the start
# -workflow, follow the rules and workflows like in part 1, except that this
# time we calculate using ranges. I'm using DFS. Search both when the rule
# is met, and when it's not met. For calculating the possible ranges for both
# outcomes, I'm using the range arithmetic from Jonathan Paulson.
A = []


def fil(rs: list, R: list):
    for r in rs[:-1]:
        if r[1] == "<":
            t = (1, r[2])
        elif r[1] == ">":
            t = (r[2] + 1, 4001)

        T = []
        F = []
        x3, x4 = t
        for x1, x2 in R[r[0]]:
            before = (x1, min(x2, x3))
            inter = (max(x1, x3), min(x2, x4))
            after = (max(x4, x1), x2)
            if before[0] < before[1]:
                F.append(before)
            if inter[0] < inter[1]:
                T.append(inter)
            if after[0] < after[1]:
                F.append(after)

        # True
        if T and not r[-1] == "R":
            TR = deepcopy(R)
            TR[r[0]] = T
            if r[-1] == "A":
                A.append(TR)
            else:
                fil(W[r[-1]], TR)

        # False
        if not F:
            return
        R[r[0]] = F
    else:
        if rs[-1] == "R":
            return
        elif rs[-1] == "A":
            A.append(R)
            return
        else:
            fil(W[rs[-1]], R)


fil(
    W["in"],
    {
        "x": [(1, 4001)],
        "m": [(1, 4001)],
        "a": [(1, 4001)],
        "s": [(1, 4001)],
    },
)

res = 0
for a in A:
    s = 1
    for v in a.values():
        tmp = 0
        for r in v:
            tmp += r[1] - r[0]
        s *= tmp
    res += s

print(f"Part 2 answer: {res}")
# ----------part 2
