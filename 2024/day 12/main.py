# ----------common for both parts
G = [s.strip("\n") for s in open("input.txt")]
w, h = len(G[0]), len(G)


def region(pos, tiles: set = None):
    x, y = pos
    if tiles is None:
        tiles = set()
        tiles.add((x, y))

    for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if not (0 <= nx < w and 0 <= ny < h):
            continue
        if (nx, ny) in tiles:
            continue
        if G[ny][nx] == G[y][x]:
            tiles.add((nx, ny))
            region((nx, ny), tiles)
    return tiles


# get all regions
all_seen = set()
regions = []
for y in range(h):
    for x in range(w):
        if (x, y) not in all_seen:
            r = region((x, y))
            regions.append(r)
            all_seen.update(r)
# ----------common for both parts


# ----------part 1
# get fence cost of all regions
fence_cost = 0
for r in regions:
    area = len(r)
    perimeter = 0
    # perimeter is easily found by finding neighbors that are different (map edge included)
    for x, y in r:
        for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
            is_out_of_bounds = not (0 <= nx < w and 0 <= ny < h)
            is_different_tile = is_out_of_bounds or G[ny][nx] != G[y][x]
            if is_out_of_bounds or is_different_tile:
                perimeter += 1
    cost = area * perimeter
    fence_cost += cost

print(f"Part 1 answer: {fence_cost}")
# ----------part 1


# ----------part 2


# This function follows the right wall until it has gone a whole loop.
# The number of sides will equal the number of turns taken.
def run(pos):
    x, y = pos
    t = G[y][x]
    dx, dy = 0, 0
    # go right until you have to turn
    while True:
        hit_edge = x + 1 == w
        hit_other_plant = x < w - 1 and G[y][x + 1] != t
        can_turn_left = y > 0 and G[y - 1][x] == t
        if hit_edge or hit_other_plant or can_turn_left:
            if can_turn_left:
                dy = -1
                x, y = x + dx, y + dy  # go one step
            else:
                dy = 1
            break
        x += 1

    tops = set()
    count = 0
    start_state = ((x, y), (dx, dy))
    while True:
        ldx, ldy = dy, -dx
        nx, ny = x + ldx, y + ldy
        in_bounds = (0 <= nx < w) and (0 <= ny < h)
        can_turn_left = in_bounds and G[ny][nx] == t
        if (dx, dy) == (1, 0) and not can_turn_left:
            tops.add((x, y))

        if can_turn_left:
            # go imediatly after turning, or else you will just spin in circles
            dx, dy = ldx, ldy
            x, y = x + dx, y + dy  # go one step
            count += 1
        else:
            nx, ny = x + dx, y + dy
            in_bounds = (0 <= nx < w) and (0 <= ny < h)
            hit_other_plant = in_bounds and G[y + dy][x + dx] != t
            need_turn_right = hit_other_plant or not in_bounds
            if need_turn_right:
                # turn right
                dx, dy = -dy, dx
                count += 1
            else:
                x, y = x + dx, y + dy  # go one step

        if ((x, y), (dx, dy)) == start_state:
            return count, tops


fence_cost = 0
for r in regions:
    area = len(r)
    side_count = 0
    tops = set()  # list of all tiles where the left-wall-run has been started at
    for x, y in r:
        # Start a left-wall-follow-run only on tiles that have
        # a different tile at the top (map edge included)
        tx, ty = x, y - 1
        is_out_of_bounds = not (0 <= tx < w and 0 <= ty < h)
        is_different_tile = is_out_of_bounds or G[ty][tx] != G[y][x]
        if is_different_tile and ((x, y) not in tops):
            count, new_tops = run((x, y))
            tops.update(new_tops)
            side_count += count
    cost = area * side_count
    fence_cost += cost


print(f"Part 2 answer: {fence_cost}")
# ----------part 2
