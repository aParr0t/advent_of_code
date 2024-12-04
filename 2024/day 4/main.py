# ----------common for both parts
from collections import defaultdict

inp = [s.strip("\n") for s in open("input.txt")]
# ----------common for both parts

# ----------part 1
directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
total = 0
word = "XMAS"
for y in range(len(inp)):
    for x in range(len(inp[y])):
        # only start searching when on an X letter
        if inp[y][x] != "X":
            continue
        # search in all directions
        for d in directions:
            _x, _y = x, y
            # go in each direction and check if the letters match
            for c in word:
                in_bounds = (0 <= _x < len(inp[y])) and (0 <= _y < len(inp))
                if not in_bounds or inp[_y][_x] != c:
                    break
                _x += d[0]
                _y += d[1]
            else:
                total += 1

print(f"Part 1 answer: {total}")
# ----------part 1

# ----------part 2
directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]  # only diagonals
total = 0
for y in range(1, len(inp) - 1):
    for x in range(1, len(inp[y]) - 1):
        # search begins in the center of the cross, an A
        if inp[y][x] != "A":
            continue
        # count letter occurrences in diagonals
        counts = defaultdict(int)
        for d in directions:
            c = inp[y + d[1]][x + d[0]]
            counts[c] += 1
        # there must be 2 S's and 2 M's in the four corners
        if not (counts["S"] == 2 and counts["M"] == 2):
            continue
        # the diagonal letters have to be opposite
        if inp[y + 1][x + 1] == inp[y - 1][x - 1]:
            continue
        total += 1

print(f"Part 2 answer: {total}")
# ----------part 2
