# ----------common for both parts
from copy import deepcopy

inp = [s.strip("\n") for s in open("input.txt")]
fall = [eval(s) for s in inp]
W = 71
simulate_count = 1024
w = h = W + 2
# set border
G_inp = [["#" for _ in range(w)] for _ in range(h)]
for y in range(1, h - 1):
    for x in range(1, w - 1):
        G_inp[y][x] = "."

start = (1, 1)
end = (w - 2, h - 2)


def bfs(G, start, end, reconstruct_path=False):
    w, h = len(G[0]), len(G)
    came_from = {}
    S = [(*start, 1)]
    seen = [[0 for _ in range(w)] for _ in range(h)]
    shortest_distance = -1
    while S:
        cur = S.pop(0)
        x, y, d = cur
        seen[y][x] = 1
        if (x, y) == end:
            shortest_distance = d - 1
            break
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if seen[ny][nx] == 1:
                continue
            if G[ny][nx] == "#":
                continue
            seen[ny][nx] = 1
            came_from[(nx, ny)] = (x, y)
            S.append((nx, ny, d + 1))

    if reconstruct_path:
        c = end
        path = [c]
        while c != start:
            if c not in came_from:
                return shortest_distance, []
            c = came_from[c]
            path.append(c)
        return shortest_distance, path
    else:
        return shortest_distance


# ----------common for both parts

# ----------part 1
G = deepcopy(G_inp)

# simulate falling bytes
for f in fall[:simulate_count]:
    G[f[1] + 1][f[0] + 1] = "#"

steps, path = bfs(G, start, end, reconstruct_path=True)

# visualization
# for x, y in path:
#     G[y][x] = "O"
# for r in G:
#     print("".join(r))

print(f"Part 1 answer: {steps}")
# ----------part 1

# ----------part 2
G = deepcopy(G_inp)

# simulate falling bytes
for f in fall[:simulate_count]:
    G[f[1] + 1][f[0] + 1] = "#"

d, path = bfs(G, start, end, reconstruct_path=True)

bad_byte = None
for f in fall[simulate_count:]:
    G[f[1] + 1][f[0] + 1] = "#"
    if (f[0] + 1, f[1] + 1) in path:
        d, path = bfs(G, start, end, reconstruct_path=True)
        if d == -1:
            bad_byte = f
            break

answer2 = f"{bad_byte[0]},{bad_byte[1]}"

print(f"Part 2 answer: {answer2}")
# ----------part 2
