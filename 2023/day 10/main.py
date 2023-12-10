# read input
inp = [s.rstrip() for s in open("input.txt")]


def get_connections(x: int, y: int):
    """The pipe must be part of the loop, because of no out-of-bounds check"""
    p = inp[y][x]
    C = []
    if p == "|":
        C.extend([(x, y + 1), (x, y - 1)])
    elif p == "-":
        C.extend([(x + 1, y), (x - 1, y)])
    elif p == "L":
        C.extend([(x, y - 1), (x + 1, y)])
    elif p == "J":
        C.extend([(x, y - 1), (x - 1, y)])
    elif p == "7":
        C.extend([(x - 1, y), (x, y + 1)])
    elif p == "F":
        C.extend([(x + 1, y), (x, y + 1)])
    elif p == "S":
        for tup in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
            if (x, y) in get_connections(*tup):
                C.append(tup)
    return C


def get_pipe(pos: tuple):
    c = pos
    pipe = []
    # find the pipe by traveling only in one direction.
    while True:
        pipe.append(c)
        C = get_connections(*c)
        c = C[0] if len(pipe) > 1 and C[0] != pipe[-2] else C[1]
        if c == pos:
            break
    return pipe


for y, l in enumerate(inp):
    for x, c in enumerate(l):
        if c == "S":
            pipe = get_pipe((x, y))

# ----------part 1
res = len(pipe) // 2

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# replace S with matching pipe type
s = pipe[0]
a, b = get_connections(*s)
D = set([(a[0] - s[0], a[1] - s[1]), (b[0] - s[0], b[1] - s[1])])
if D == set([(0, 1), (0, -1)]):
    r = "|"
elif D == set([(1, 0), (-1, 0)]):
    r = "-"
elif D == set([(0, -1), (1, 0)]):
    r = "L"
elif D == set([(0, -1), (-1, 0)]):
    r = "J"
elif D == set([(0, 1), (-1, 0)]):
    r = "7"
elif D == set([(0, 1), (1, 0)]):
    r = "F"
inp[s[1]] = inp[s[1]].replace("S", r)

# for every tile, check if it's inside or outside. Since a loop can be
# thought of as a polygon, we can use the ray casting algorithm for checking
# if a point is inside a polygon. This code sends out
# vertical (towards north) rays. An edge case occurs when the ray passes
# through a vertical edge. To solve it, I imagined that all vertical lines
# are tilted 45 degrees. So a vertical edge will either have corners
# going in opposite horizontal directions, or not. When the corners have
# opposite horizontal-directions, the ray should intersect it, and otherwise not
# opposite corners:
# ..........         ..........
# .----7....   --->  ----7.....
# .....|....         .....\....
# .....L----         ......L---
# ..........         ..........
# equal corners:
# ..........         ..........
# .....F----   --->  ....F-----
# .....|....         .....\....
# .....L----         ......L---
# ..........         ..........

C = {"7": "L", "F": "J"}
w, h = len(inp[0]), len(inp)
res = 0
for x in range(w):
    inside = False
    prev_corner = ""
    for y in range(h):
        pos = (x, y)
        c = inp[y][x]
        if pos in pipe:
            if c == "|":
                continue

            is_opposite_corners = prev_corner in C and c == C[prev_corner]
            if c == "-" or is_opposite_corners:
                inside = not inside
            if c != "-":
                prev_corner = c
        elif inside:
            res += 1
            # for drawing the map with enclosed tiles
            # l = inp[y]
            # inp[y] = l[:x] + "@" + l[x + 1 :]

print(f"Part 2 answer: {res}")
# ----------part 2
