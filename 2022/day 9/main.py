# read input
inp = [s.rstrip("\n").split(" ") for s in open("input.txt")]
motions = [(x, int(y)) for (x, y) in inp]

# ----------both parts
def move(start, step):
    return [start[0] + step[0], start[1] + step[1]]


# ----------both parts

# ----------part 1
def adjust_tail():
    global head
    global tail
    dx, dy = head[0] - tail[0], head[1] - tail[1]
    abs_dx, abs_dy = abs(dx), abs(dy)

    if abs_dx == 1 and abs_dy == 1:
        return

    # up or down
    if abs_dx == 0:
        if abs_dy <= 1:
            return

    # left or right
    if abs_dy == 0:
        if abs_dx <= 1:
            return

    tail = prev_head.copy()


visited = set()
head = [0, 0]
prev_head = head.copy()
tail = head.copy()
visited.add(str(tail))
for direction_code, steps_left in motions:
    match direction_code:
        case "U":
            direction = (0, 1)
        case "R":
            direction = (1, 0)
        case "D":
            direction = (0, -1)
        case "L":
            direction = (-1, 0)

    while steps_left > 0:
        prev_head = head.copy()
        head = move(head, direction)
        adjust_tail()
        visited.add(str(tail))
        steps_left -= 1

print(f"Part 1 answer: {len(visited)}")
# ----------part 1

# ----------part 2
def adjust_knot(a, b):
    dx, dy = (
        a[0] - b[0],
        a[1] - b[1],
    )
    abs_dx, abs_dy = abs(dx), abs(dy)

    if abs_dx == 1 and abs_dy == 1:
        return b

    # up or down
    if abs_dx == 0:
        if abs_dy <= 1:
            return b
        return move(b, [dx, dy // 2])

    # left or right
    if abs_dy == 0:
        if abs_dx <= 1:
            return b
        return move(b, [dx // 2, dy])

    if abs_dx == 2 and abs_dy == 2:
        return move(b, [dx // 2, dy // 2])

    if abs_dy == 2:
        return move(b, [dx, dy // 2])

    if abs_dx == 2:
        return move(b, [dx // 2, dy])


visited = set()
knot_count = 10
knots = [[0, 0] for _ in range(knot_count)]
visited.add(str(knots[-1]))

for direction_code, steps_left in motions:
    match direction_code:
        case "U":
            direction = (0, 1)
        case "R":
            direction = (1, 0)
        case "D":
            direction = (0, -1)
        case "L":
            direction = (-1, 0)

    while steps_left > 0:
        knots[0] = move(knots[0], direction)
        for i in range(knot_count - 1):
            knots[i + 1] = adjust_knot(knots[i], knots[i + 1])

        visited.add(str(knots[-1]))
        steps_left -= 1


print(f"Part 2 answer: {len(visited)}")
# ----------part 2
