# read input
paths = [s.rstrip("\n").split(" -> ") for s in open("input.txt")]


# ----------both parts
def init_cave():
    cave_w, cave_h = 1000, 200
    cave = [["." for x in range(cave_w)] for y in range(cave_h)]

    for path in paths:

        def string_to_cord(string):
            return [int(x) for x in string.split(",")]

        px, py = string_to_cord(path[0])
        for cord_string in path[1:]:
            x, y = string_to_cord(cord_string)
            dx, dy = x - px, y - py

            if dx == 0:
                dy_sign = dy // abs(dy)
                for y in range(py, py + dy + dy_sign, dy_sign):
                    cave[y][x] = "#"
            if dy == 0:
                dx_sign = dx // abs(dx)
                for x in range(px, px + dx + dx_sign, dx_sign):
                    cave[y][x] = "#"

            px, py = x, y
    return cave


sand_spawn = (500, 0)
moves = [(0, 1), (-1, 1), (1, 1)]
# ----------both parts

# ----------part 1
cave = init_cave()
sand_overflow = False
sand_count = 0

while not sand_overflow:
    sand_x, sand_y = sand_spawn

    is_stable = False
    while not is_stable and not sand_overflow:
        for move_x, move_y in moves:
            # chech sand fall into abyss
            if sand_y + move_y >= len(cave):
                sand_overflow = True
                break

            if cave[sand_y + move_y][sand_x + move_x] == ".":
                sand_x += move_x
                sand_y += move_y
                break
        else:
            is_stable = True
            sand_count += 1
            cave[sand_y][sand_x] = "o"

print(f"Part 1 answer: {sand_count}")
# ----------part 1

# ----------part 2
cave = init_cave()

# find lowest point in cave
for y in range(len(cave) - 1, -1, -1):
    if "#" in cave[y]:
        ground = y + 2
        cave[ground] = list("#" * len(cave[0]))
        del cave[ground + 1 :]
        break

total_rest = False
sand_count = 0

while not total_rest:
    sand_x, sand_y = sand_spawn

    is_stable = False
    while not is_stable and not total_rest:
        for move_x, move_y in moves:
            if cave[sand_y + move_y][sand_x + move_x] == ".":
                sand_x += move_x
                sand_y += move_y
                break
        else:
            if (sand_x, sand_y) == sand_spawn:
                total_rest = True
            is_stable = True
            sand_count += 1
            cave[sand_y][sand_x] = "o"

print(f"Part 2 answer: {sand_count}")
# ----------part 2
