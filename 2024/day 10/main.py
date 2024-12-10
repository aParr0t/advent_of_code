# ----------common for both parts
inp = [s.strip("\n") for s in open("input.txt")]
G = [[int(x) if x != "." else "." for x in s] for s in inp]

w, h = len(G[0]), len(G)
# ----------common for both parts


# ----------part 1
heads = set()


def search1(pos: tuple, f: tuple):
    x, y = pos
    cur = G[y][x]
    if cur == 9:
        heads.add((x, y))

    for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if not (0 <= nx < w and 0 <= ny < h):
            continue
        if (nx, ny) == f:
            continue
        if G[ny][nx] != cur + 1:
            continue
        search1((nx, ny), pos)


total = 0
for y in range(h):
    for x in range(w):
        if G[y][x] == 0:
            # search
            heads.clear()
            t = search1((x, y), (x, y))
            total += len(heads)

print(f"Part 1 answer: {total}")
# ----------part 1


# ----------part 2
def search2(pos: tuple, f: tuple):
    x, y = pos
    cur = G[y][x]
    if cur == 9:
        return 1

    total = 0
    for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if not (0 <= nx < w and 0 <= ny < h):
            continue
        if (nx, ny) == f:
            continue
        if G[ny][nx] != cur + 1:
            continue
        total += search2((nx, ny), pos)
    return total


total = 0
for y in range(h):
    for x in range(w):
        if G[y][x] == 0:
            # search
            t = search2((x, y), (x, y))
            total += t

print(f"Part 2 answer: {total}")
# ----------part 2
