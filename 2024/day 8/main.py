# ----------common for both parts
import itertools
from collections import defaultdict

inp = [s.strip("\n") for s in open("input.txt")]
w, h = len(inp[0]), len(inp)

antenna_map = defaultdict(list)
for y in range(h):
    for x in range(w):
        if inp[y][x] != ".":
            antenna = inp[y][x]
            antenna_map[antenna].append((x, y))
# ----------common for both parts

# ----------part 1
antinodes = set()
for antenna_type, antennas in antenna_map.items():
    # get all combinations of the antennas with the same frequency
    combinations = itertools.combinations(antennas, 2)
    for combination in combinations:
        # get all combinations of the antennas with the same frequency
        a, b = combination
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        anti = []
        anti.append((a[0] - dx, a[1] - dy))
        anti.append((b[0] + dx, b[1] + dy))

        # filter out antennas that are outside of the map
        for a in anti:
            if (0 <= a[0] < w) and (0 <= a[1] < h):
                antinodes.add(a)

antinode_count = len(antinodes)
print(f"Part 1 answer: {antinode_count}")
# ----------part 1

# ----------part 2
antinodes = set()
for antenna_type, antennas in antenna_map.items():
    # get all combinations of the antennas with the same frequency
    combinations = itertools.combinations(antennas, 2)
    for combination in combinations:
        # calculate the step distance between each antinode
        a, b = combination
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        anti = []

        # go in a line in both directions and save the antinodes
        pos = a
        while (0 <= pos[0] < w) and (0 <= pos[1] < h):
            anti.append(pos)
            pos = (pos[0] + dx, pos[1] + dy)
        pos = a
        while (0 <= pos[0] < w) and (0 <= pos[1] < h):
            anti.append(pos)
            pos = (pos[0] - dx, pos[1] - dy)

        # filter out antennas that are outside of the map
        for a in anti:
            if (0 <= a[0] < w) and (0 <= a[1] < h):
                antinodes.add(a)

antinode_2_count = len(antinodes)

print(f"Part 2 answer: {antinode_2_count}")
# ----------part 2
