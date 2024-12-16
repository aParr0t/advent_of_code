# ----------common for both parts
import heapq
from collections import defaultdict

G = [s.strip("\n") for s in open("input.txt")]
w, h = len(G[0]), len(G)

start_pos = 1, h - 2
start_direction = (1, 0)
end = (w - 2, 1)


# A* implementation taken from: https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
def heuristic(x, y, dx, dy):
    cost = end[0] - x + end[1] - y
    cost += 1000
    if dx == -1 or dy == -1:
        cost += 1000
    return cost


x, y = start_pos
dx, dy = start_direction

came_from = {}

g_score = defaultdict(lambda: float("inf"))
g_score[(x, y, dx, dy)] = 0

f_score = defaultdict(lambda: float("inf"))
f_score[(x, y, dx, dy)] = heuristic(x, y, dx, dy)
open_set = [(f_score[(x, y, dx, dy)], (x, y, dx, dy))]

while open_set:
    _, current = heapq.heappop(open_set)
    x, y, dx, dy = current
    if (x, y) == end:
        print("found shortest path!")
        break

    ldx, ldy = dy, -dx
    rdx, rdy = -dy, dx
    for nx, ny, ndx, ndy, d in [
        (x + dx, y + dy, dx, dy, 1),  # x, y, dx, dy, d(current, neighbor)
        (x, y, ldx, ldy, 1000),
        (x, y, rdx, rdy, 1000),
    ]:
        if G[ny][nx] == "#":
            continue
        tentative_score = g_score[(x, y, dx, dy)] + d
        if tentative_score < g_score[(nx, ny, ndx, ndy)]:
            came_from[(nx, ny, ndx, ndy)] = (x, y, dx, dy)
            g_score[(nx, ny, ndx, ndy)] = tentative_score
            f_score[(nx, ny, ndx, ndy)] = tentative_score + heuristic(nx, ny, ndx, ndy)
            if (nx, ny, ndx, ndy) not in open_set:
                heapq.heappush(
                    open_set, (f_score[(nx, ny, ndx, ndy)], (nx, ny, ndx, ndy))
                )

shortest_path = min(
    [g_score[(end[0], end[1], dx, dy)] for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
)
# ----------common for both parts


# ----------part 1
print(f"Part 1 answer: {shortest_path}")
# ----------part 1

# ----------part 2
total_path = set()
stack = [(end[0], end[1], 1, 0), (end[0], end[1], 0, -1)]
while stack:
    current = stack.pop(-1)
    x, y, dx, dy = current
    ldx, ldy = dy, -dx
    rdx, rdy = -dy, dx
    g_current = g_score[(x, y, dx, dy)]
    if g_current > shortest_path:
        continue
    for nx, ny, ndx, ndy, d in [
        (x - dx, y - dy, dx, dy, 1),  # x, y, dx, dy, d(current, neighbor)
        (x, y, ldx, ldy, 1000),
        (x, y, rdx, rdy, 1000),
    ]:
        g_neighbor = g_score[(nx, ny, ndx, ndy)]
        if g_current - g_neighbor == d:
            stack.append((nx, ny, ndx, ndy))
            total_path.add((nx, ny))

answer = len(total_path) + 1  # -1 because start gets added to total path

# visualization
# for y in range(h):
#     for x in range(w):
#         if (x, y) in total_path:
#             print("O", end="")
#         else:
#             print(G[y][x], end="")
#     print()

print(f"Part 2 answer: {answer}")
# ----------part 2
