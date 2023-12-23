# read input
IN = [s.rstrip() for s in open("input.txt")]
for i in range(len(IN)):
    d, l, col = IN[i].split()
    l = int(l)
    col = col[1:-1]
    IN[i] = (d, l, col)

# ----------part 1
# Used a straight forward flood fill approach. Instead of filling the inside
# of the digging, I fill the outside, and calculate the dug area by
# subtracting the outside area from the total area. This approach is
# slower than the one for part 2 lol.

# find bounding box
x = y = 0
min_x = min_y = 0
max_x = max_y = 0
for d, l, col in IN:
    if d == "U":
        y -= l
    elif d == "D":
        y += l
    elif d == "L":
        x -= l
    elif d == "R":
        x += l
    min_x, min_y = min(min_x, x), min(min_y, y)
    max_x, max_y = max(max_x, x), max(max_y, y)

bw, bh = max_x - min_x + 1, max_y - min_y + 1
G = [["." for x in range(bw + 2)] for y in range(bh + 2)]
w, h = len(G[0]), len(G)


# dig
x, y = -min_x + 1, -min_y + 1
for d, l, col in IN:
    px, py = x, y
    if d == "U":
        y -= l
    elif d == "D":
        y += l
    elif d == "L":
        x -= l
    elif d == "R":
        x += l
    dx = 1 if x - px >= 0 else -1
    dy = 1 if y - py >= 0 else -1
    for _y in range(py, y + dy, dy):
        for _x in range(px, x + dx, dx):
            G[_y][_x] = "#"

# flood fill outside
V = set()
TV = [(0, 0)]
empty = 0
while TV:
    (_x, _y) = TV.pop()
    for x, y in [
        (_x - 1, _y),
        (_x + 1, _y),
        (_x, _y - 1),
        (_x, _y + 1),
    ]:
        if not (0 <= x < w) or not (0 <= y < h):
            continue

        if (x, y) in V:
            continue
        V.add((x, y))
        if G[y][x] == "#":
            continue
        empty += 1
        TV.append((x, y))

res = w * h - empty

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# finding the dug area by summing the tiles of the edges together with the
# tiles inside the edges. Finding the edge tiles is the easy part. Finding
# the inside tiles is much more difficult. Each horizontal digging
# is either left-going or right-going. Then, a tile is inside if the
# lower horizontal edge is left-going and the upper horizontal edge is
# right-going. The algorithm goes through all the edges that are right-going,
# and checks which horizontal left-going edges it intersects with on
# the way up.

x = y = 0
hg1 = 0
H = []  # (range, height, direction)
VEND = []  # (x, y)
edge_tiles = 0
for d, l, col in IN:
    w = int(col[1:-1], base=16)
    d = int(col[-1])

    px, py = x, y
    if d == 3 or d == "U":
        y -= w
    elif d == 1 or d == "D":
        y += w
    elif d == 2 or d == "L":
        x -= w
    elif d == 0 or d == "R":
        x += w

    dx = x - px
    dy = y - py
    if dy != 0:
        hg1 += dy
        VEND.append((x, max(y, py)))
    else:
        a, b = min(px, x), max(px, x)
        dr = "L" if d == 2 or d == "L" else "R"
        H.append(((a, b), hg1, dr))
    edge_tiles += abs(dx + dy)


H.sort(key=lambda x: x[1])
res = 0
for i, h in enumerate(H):
    r1, hg1, dr = h
    if dr == "R":
        continue

    x1, x2 = r1
    if (x1, hg1) in VEND:
        x1 += 1
    if (x2, hg1) not in VEND:
        x2 += 1
    R = [(x1, x2)]
    i2 = i
    while R:
        i2 -= 1
        h2 = H[i2]
        if h2[2] == "L":
            continue

        x3, x4 = h2[0]
        x4 += 1
        NR = []
        for r1 in R:
            x1, x2 = r1
            before = (x1, min(x2, x3))
            inter = (max(x1, x3), min(x2, x4))
            after = (max(x4, x1), x2)
            if before[1] > before[0]:
                NR.append(before)
            if inter[1] > inter[0]:
                w = inter[1] - inter[0]
                hg = hg1 - h2[1] - 1
                res += w * hg
            if after[1] > after[0]:
                NR.append(after)
        R = NR

res += edge_tiles

print(f"Part 2 answer: {res}")
# ----------part 2
