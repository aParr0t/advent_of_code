# read input
inp = [s.rstrip() for s in open("input.txt")]


# ----------part 1
# expand rows
_inp = [l for l in inp]
for i in range(len(_inp) - 1, -1, -1):
    l = _inp[i]
    if "#" in l:
        continue
    _inp.insert(i + 1, "." * len(_inp[0]))

# expand cols
for i in range(len(_inp[0]) - 1, -1, -1):
    col = "".join([l[i] for l in _inp])
    if "#" in col:
        continue
    for j in range(len(_inp)):
        l = _inp[j]
        _inp[j] = l[:i] + ".." + l[i + 1 :]

# find galaxies
G = []
for y in range(len(_inp)):
    for x in range(len(_inp[0])):
        if _inp[y][x] == "#":
            G.append((x, y))

# calculate distances
res = 0
for i, g1 in enumerate(G[:-1]):
    for g2 in G[i + 1 :]:
        res += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# the code for part two could also be used for part 1, but I want to show
# my solution for part 1

# find galaxies
G = []
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == "#":
            G.append((x, y))

# create boolean lists for faster lookup of empty columns/rows
rows = ["#" in l for l in inp]
cols = []
for i in range(len(inp[0])):
    cols.append("#" in "".join([inp[j][i] for j in range(len(inp))]))

exp = 1000000
res = 0
for i, g1 in enumerate(G[:-1]):
    for g2 in G[i + 1 :]:
        dx = dy = 0
        a, b = sorted([g1[0], g2[0]])
        for x in range(a, b):
            if cols[x]:
                dx += 1
            else:
                dx += exp
        a, b = sorted([g1[1], g2[1]])
        for y in range(a, b):
            if rows[y]:
                dy += 1
            else:
                dy += exp
        res += dx + dy


print(f"Part 2 answer: {res}")
# ----------part 2
