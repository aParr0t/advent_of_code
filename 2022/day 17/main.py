# read input
jets = [1 if s == ">" else -1 for s in open("input.txt").readline().rstrip()]

# ----------both parts
jets_len = len(jets)
rocks = [
    ["####"],
    [".#.", "###", ".#."],
    ["..#", "..#", "###"],
    ["#", "#", "#", "#"],
    ["##", "##"],
]
# ----------both parts

# ----------part 1
def move_valid(rock, x, y, mx, my):
    rock_w = len(rock[0])
    for ry in range(len(rock)):
        for rx in range(rock_w):
            if rock[-1 - ry][rx] == ".":
                continue
            cx, cy = x + rx + mx, y + ry + my
            if cx < 0 or cx >= tower_w or cy < 0:
                return False
            if tower[cy][cx] == "#":
                return False
    return True


tower_w = 7
tower = [["." for x in range(tower_w)] for y in range(4)]
jet_idx = 0
for r_idx in range(2022):
    # find the highest rock
    highest_rock = -1
    for y in range(len(tower) - 1, -1, -1):
        if "#" in tower[y]:
            highest_rock = y
            break

    # spawn new rock
    rx = 2
    ry = highest_rock + 4
    rock = rocks[r_idx % len(rocks)]

    # extend tower
    extend_height = len(rock) + ry - len(tower)
    for _ in range(extend_height):
        tower.append(["." for x in range(tower_w)])

    # simulate rock falling down
    while True:
        px, py = rx, ry

        # push by jet
        j = jets[jet_idx % len(jets)]
        jet_idx += 1
        if move_valid(rock, rx, ry, j, 0):
            rx += j

        # fall down
        if move_valid(rock, rx, ry, 0, -1):
            ry -= 1

        # check if stable
        if ry == py:
            break

    # save rock to tower
    rock_w = len(rock[0])
    for i in range(len(rock)):
        for j in range(rock_w):
            if rock[-1 - i][j] == ".":
                continue
            tower[ry + i][rx + j] = "#"

for y in range(len(tower) - 1, -1, -1):
    if "#" in tower[y]:
        highest_rock = y + 1
        break

print(f"Part 1 answer: {highest_rock}")
# ----------part 1

# ----------part 2
# ----------part 2
