# ----------common for both parts
from copy import deepcopy

inp_G = [s.strip("\n") for s in open("input.txt")]
w, h = len(inp_G[0]), len(inp_G)

# find the starting position and direction of the guard
start_pos = None
joined = "".join(inp_G)
directions = ((">", (1, 0)), ("^", (0, -1)), ("<", (-1, 0)), ("v", (0, 1)))
start_direction = None
for c, d in directions:
    if c in joined:
        i = joined.index(c)
        start_pos = (i % w, i // w)
        start_direction = d
        break


def mark(pos, c="X"):
    """Marks a tile on the grid"""
    s = G[pos[1]]
    G[pos[1]] = s[: pos[0]] + c + s[pos[0] + 1 :]


# ----------common for both parts

# ----------part 1
G = deepcopy(inp_G)
pos = start_pos
direction = start_direction

# simulate guard walking
while (0 < pos[0] < w - 1) and (0 < pos[1] < h - 1):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    next_tile = G[next_pos[1]][next_pos[0]]
    mark(pos, "X")
    if next_tile == "#":
        # turn right (-y, x)
        direction = (-direction[1], direction[0])
    else:
        pos = next_pos
mark(pos, "X")

# count number of visited places
total = 0
for s in G:
    total += s.count("X")

# print the grid
# for s in G:
#     print(s)

print(f"Part 1 answer: {total}")
# ----------part 1

# ----------part 2
G = deepcopy(inp_G)
pos = start_pos
direction = start_direction


def will_enter_loop(start_pos, start_direction):
    """Checks if the guard will enter a loop in the current grid"""
    pos, direction = start_pos, start_direction
    # stores the obstacles hit and from which direction they were hit
    # if an obstacle gets hit a second time from the same direction,
    # then that means the guard has entered a loop
    ob_hit = set()
    while (0 < pos[0] < w - 1) and (0 < pos[1] < h - 1):
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
        next_tile = G[next_pos[1]][next_pos[0]]

        if next_tile == "#":
            if (next_pos, direction) in ob_hit:
                return True
            ob_hit.add((next_pos, direction))
            # turn right (-y, x)
            direction = (-direction[1], direction[0])
        else:
            pos = next_pos
    return False


# simulate guard walking
obstacles = set()
while (0 < pos[0] < w - 1) and (0 < pos[1] < h - 1):
    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
    next_tile = G[next_pos[1]][next_pos[0]]
    mark(pos, "@")  # mark the path of the guard
    if next_tile == "#":
        # turn right (-y, x)
        direction = (-direction[1], direction[0])
    else:
        # an obstacle can't be placed on already visited tiles because
        # that would prevent the guard from reaching this position
        # in the first place
        if (next_pos != start_pos) and (next_tile != "@"):
            # temporarily place the obstacle and check if the guard enters a loop.
            # after the check, remove the obstacle
            mark(next_pos, "#")
            if will_enter_loop(pos, direction):
                obstacles.add(next_pos)
            mark(next_pos, ".")
        pos = next_pos

obstacle_count = len(obstacles)
print(f"Part 2 answer: {obstacle_count}")
# ----------part 2
