import functools
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)

R = []
for l in L:
    p, v = l.split(" @ ")
    p = [int(x) for x in p.split(", ")]
    v = [int(x) for x in v.split(", ")]
    R.append((p, v))


# ----------part 1
# I actually managed to do part 1 all by myself, without looking up a single
# thing. Did it first on paper, and then implemented it. I had learned
# the general equations in 12th grade, and just had to adjust them for this
# problem.
def is_inside(r1, r2, low: int, high: int):
    # dumb fking check because I came up with the maths myself
    # I know wikipedia has a brilliant page about it
    (px, py, _), (vpx, vpy, _) = r1
    (qx, qy, _), (vqx, vqy, _) = r2
    num_s = py + (vpy / vpx) * (qx - px) - qy
    den_s = vqy - ((vqx * vpy) / vpx)

    if den_s == 0:
        # parallel
        a = vpx / vpy
        b1 = py - a * px
        b2 = qy - a * qx
        if b1 != b2:
            # parallel but not coinciding
            return False
        else:
            # parallel and coinciding
            pass
    else:
        s = num_s / den_s
        if s <= 0:
            return False
        x = qx + s * vqx
        y = qy + s * vqy
        if (low <= x <= high) and (low <= y <= high):
            return True
        else:
            return False
    return False


res = 0
low = 200000000000000
high = 400000000000000
for i in range(len(R) - 1):
    r1 = R[i]
    for j in range(i + 1, len(R)):
        r2 = R[j]
        # dumb fking check because I came up with the maths myself
        # I know wikipedia has a brilliant page about it
        inside = is_inside(r1, r2, low, high) and is_inside(r2, r1, low, high)
        if inside:
            res += 1


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# Honestly, part 2 was bs. Cool to learn about this z3 library and the stuff
# it can do, but not knowing about it can make you lose countless hours
# solving the unsolvable. Got help from Jonathan Paulson:
# https://www.youtube.com/watch?v=vZa2jErpSg8
import z3

# somehow z3.Int() doesn't work. The program never finishes. z3.Real() on the
# other hand finishes almost instantly.
x = z3.Real("x")
y = z3.Real("y")
z = z3.Real("z")
vx = z3.Real("vx")
vy = z3.Real("vy")
vz = z3.Real("vz")

solver = z3.Solver()
T = [z3.Real(f"T{i}") for i in range(len(R))]
for i, r in enumerate(R):
    (rx, ry, rz), (rvx, rvy, rvz) = r
    solver.add(x + vx * T[i] == rx + rvx * T[i])
    solver.add(y + vy * T[i] == ry + rvy * T[i])
    solver.add(z + vz * T[i] == rz + rvz * T[i])

solver.check()
m = solver.model()
res = m.eval(x + y + z)

print(f"Part 2 answer: {res}")
# ----------part 2
