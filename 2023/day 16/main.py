# read input
IN = [s.rstrip() for s in open("input.txt")]

w, h = len(IN[0]), len(IN)


def shoot(x, y, dx, dy):
    B = [(x, y, dx, dy)]  # (x, y), (x_dir, y-dir)
    V = set()  # visited
    v_len = 0
    v_count = 0
    while B:
        NB = set()
        for b in B:
            b = list(b)
            x, y, dx, dy = b
            if not (0 <= x < w) or not (0 <= y < h):
                continue
            V.add((x, y))

            # move beam
            t = IN[y][x]
            if t == "-":
                if dy != 0:
                    NB.add((x - 1, y, -1, 0))
                    NB.add((x + 1, y, 1, 0))
                    continue
            elif t == "|":
                if dx != 0:
                    NB.add((x, y - 1, 0, -1))
                    NB.add((x, y + 1, 0, 1))
                    continue
            elif t == "\\":
                if dx == 1:
                    b = [x, y + 1, 0, 1]
                elif dx == -1:
                    b = [x, y - 1, 0, -1]
                elif dy == 1:
                    b = [x + 1, y, 1, 0]
                elif dy == -1:
                    b = [x - 1, y, -1, 0]
            elif t == "/":
                if dx == 1:
                    b = [x, y - 1, 0, -1]
                elif dx == -1:
                    b = [x, y + 1, 0, 1]
                elif dy == 1:
                    b = [x - 1, y, -1, 0]
                elif dy == -1:
                    b = [x + 1, y, 1, 0]

            if b[0] == x and b[1] == y:
                b[0] = x + dx
                b[1] = y + dy
            NB.add(tuple(b))

        B = list(NB)

        if len(V) != v_len:
            v_len = len(V)
            v_count = 0
        else:
            v_count += 1
            if v_count > 2:
                break

    return len(V)


# ----------part 1
# decided to go for bfs, but i think it was a mistake. I think dfs would've
# allowed me to cache beam paths between obstacles. Then when other beams
# would pass an already visited obstacle, they could just lookup the path.

res = shoot(0, 0, 1, 0)

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
mx = 0
for y, dy in [(0, 1), (h - 1, -1)]:
    for x in range(w):
        mx = max(mx, shoot(x, y, 0, dy))
for x, dx in [(0, 1), (w - 1, -1)]:
    for y in range(h):
        mx = max(mx, shoot(x, y, dx, 0))

res = mx

print(f"Part 2 answer: {res}")
# ----------part 2
