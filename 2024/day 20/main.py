# ----------common for both parts
G = [s.strip("\n") for s in open("input.txt")]

w, h = len(G[0]), len(G)
start = end = None
for y in range(h):
    for x in range(w):
        match G[y][x]:
            case "S":
                start = (x, y)
            case "E":
                end = (x, y)

# Calculate path distances
d = 0
x, y = start
dist = {}
dist[start] = 0
came_from = {}
while (x, y) != end:
    d += 1
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if G[ny][nx] == "#":
            continue
        if (nx, ny) in dist:
            continue
        came_from[(nx, ny)] = (x, y)
        dist[(nx, ny)] = d
        x, y = nx, ny
# ----------common for both parts

# ----------part 1
# find shortcuts
x, y = end
total = 0
found_start = False
while not found_start:
    if (x, y) == start:
        found_start = True
    for nx, ny in [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]:
        if not (0 <= nx < w and 0 <= ny < h):
            continue
        if G[ny][nx] == "#":
            continue
        shortcut = dist[(nx, ny)] - dist[(x, y)]
        shortcut -= 2  # it takes two seconds to take the shortcut
        if shortcut >= 100:
            total += 1
    if not found_start:
        x, y = came_from[(x, y)]

print(f"Part 1 answer: {total}")
# ----------part 1

# ----------part 2
from collections import defaultdict

x, y = end
counts = defaultdict(int)
found_start = False
cheat_dist = 20
while not found_start:
    if (x, y) == start:
        found_start = True
    for ny in range(y - cheat_dist, y + cheat_dist + 1):
        for nx in range(x - cheat_dist, x + cheat_dist + 1):
            if not (0 <= nx < w and 0 <= ny < h):
                continue
            d = abs(nx - x) + abs(ny - y)
            if d > cheat_dist:
                continue
            if G[ny][nx] == "#":
                continue
            shortcut = abs(dist[(nx, ny)] - dist[(x, y)])
            shortcut -= d  # it takes some seconds to take the shortcut
            counts[shortcut] += 1
    if not found_start:
        x, y = came_from[(x, y)]

# all shortcuts have been double counted
for k in counts:
    counts[k] //= 2

# count more than 100
total = 0
for k, v in counts.items():
    if k >= 100:
        total += v

print(f"Part 2 answer: {total}")
# ----------part 2
