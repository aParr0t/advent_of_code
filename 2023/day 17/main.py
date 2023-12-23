import heapq
from collections import defaultdict, deque

# read input
IN = [[int(x) for x in s.rstrip()] for s in open("input.txt")]

w, h = len(IN[0]), len(IN)

# ----------part 1
# Day 17 was suuuper difficult. I managed to do part 1 by myself. The solution
# takes about 10-15s. My solution is using dijkstra's algorithm, but on a
# more complex grid. It's important to consider a node's travel length in one
# direction and also in what direction it's pointing.

e = (w - 1, h - 1)
s = (0, 0)
TV = [(s, 0, 0, 0, set())]  # TO visit [(pos, dir, cost, length, from)]
E = []  # ends
F = defaultdict(set)  # from-visits
L = defaultdict(lambda: 999)  # lengths
DR = defaultdict(set)  # directions

while TV:
    TV.sort(key=lambda x: x[2], reverse=True)
    c = TV.pop()
    (x, y), dr, cost, l, f = c

    if (x, y) == e:
        E.append(c)

    for pd, nd, nx, ny in [
        (0, 2, x - 1, y),
        (1, 3, x, y + 1),
        (2, 0, x + 1, y),
        (3, 1, x, y - 1),
    ]:
        if dr != pd:
            if not (0 <= nx < w) or not (0 <= ny < h):
                continue
            if (nx < 113) and (20 < ny):
                continue

            npos = (nx, ny)
            ncost = cost + IN[ny][nx]

            if (x, y) in F[npos]:
                if l < L[(x, y)]:
                    pass
                else:
                    if dr in DR[(x, y)]:
                        continue

            if dr == nd:
                nl = l + 1
                if nl == 4:
                    continue
            else:
                nl = 1

            TV.append((npos, nd, ncost, nl, set([*f, (x, y)])))
            F[npos].add((x, y))
    L[(x, y)] = l
    DR[(x, y)].add(dr)

min_p = min(E, key=lambda x: x[2])
res = min_p[2]

# print path
# _IN = [ar.copy() for ar in IN]
# for y in range(h):
#     for x in range(w):
#         if (x, y) in min_p[4]:
#             _IN[y][x] = "\x1b[6;30;42m" + str(_IN[y][x]) + "\x1b[0m"
# for r in _IN:
#     print("".join([str(s) for s in r]))

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# I didn't manage to do part 2 in time. Had to get help from Jonathan Paulson's
# video for this day. He used the heapq library, which kinda is essential for
# dijkstra's algorithm unless you sort the queue each time, but that is slower.
# In other words, I forgot the important bit of dijkstra's algorithm, which is
# to pick the node with the lowest distance. My first failing solution gave me
# the answer 837 which was very close to the real answer 822 :(

s = (0, 0)
O = [(0, s, 0, 0), (0, s, 3, 0)]  # TO visit [(dist, pos, dir, length)]
D = {}
while O:
    c = heapq.heappop(O)
    dist, (x, y), dr, l = c
    if (x, y, dr, l) in D:
        continue
    else:
        D[(x, y, dr, l)] = dist

    for pd, nd, nx, ny in [
        (2, 0, x + 1, y),
        (1, 3, x, y + 1),
        (0, 2, x - 1, y),
        (3, 1, x, y - 1),
    ]:
        if dr == pd:
            continue

        if not (0 <= nx < w) or not (0 <= ny < h):
            continue

        npos = (nx, ny)
        ndist = dist + IN[ny][nx]

        if dr == nd:
            nl = l + 1
            if nl > 10:
                continue
        elif dr != nd and not (4 <= l <= 10):
            continue
        else:
            nl = 1
        heapq.heappush(O, (ndist, npos, nd, nl))

res = 9999999
for (x, y, dr, l), d in D.items():
    if x == w - 1 and y == h - 1 and (4 <= l <= 10):
        res = min(res, d)

print(f"Part 2 answer: {res}")
# ----------part 2
