# ----------common for both parts
from copy import deepcopy

inp = [s.strip("\n") for s in open("input.txt")]
G_inp = [[c for c in s] for s in inp[: inp.index("")]]
moves = "".join(inp[inp.index("") + 1 :])
robot_start = None
w, h = len(G_inp[0]), len(G_inp)
for y in range(h):
    for x in range(w):
        if G_inp[y][x] == "@":
            robot_start = (x, y)
            break
move_map = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}

# ----------common for both parts

# ----------part 1
G = deepcopy(G_inp)
x, y = robot_start
for m in moves:
    dx, dy = move_map[m]
    nx, ny = x + dx, y + dy
    nt = G[ny][nx]
    if nt == "#":
        continue
    elif nt == ".":
        G[y][x] = "."
        G[ny][nx] = "@"
        x, y = nx, ny
    elif nt == "O":
        _x, _y = nx, ny
        while True:
            _x, _y = _x + dx, _y + dy
            _t = G[_y][_x]
            if _t == "#":
                break
            elif _t == ".":
                G[_y][_x] = "O"
                G[ny][nx] = "@"
                G[y][x] = "."
                x, y = nx, ny
                break

# calculate GPS
total = 0
for y in range(h):
    for x in range(w):
        if G[y][x] == "O":
            total += y * 100 + x

print(f"Part 1 answer: {total}")
# ----------part 1

# ----------part 2
G = []
for y in range(h):
    G.append("")
    for x in range(w):
        t = G_inp[y][x]
        if t == "#":
            G[y] += "##"
        elif t == "O":
            G[y] += "[]"
        elif t == "@":
            G[y] += "@."
        elif t == ".":
            G[y] += ".."
    G[y] = [c for c in G[y]]

# print("start")
# for r in G:
#     print("".join(r))

robot_start = None
w, h = len(G[0]), len(G)
for y in range(h):
    for x in range(w):
        if G[y][x] == "@":
            robot_start = (x, y)
            break
x, y = robot_start
for m in moves:
    # input()
    # print(m)
    dx, dy = move_map[m]
    nx, ny = x + dx, y + dy
    nt = G[ny][nx]
    if nt == "#":
        pass
    elif nt == ".":
        G[y][x] = "."
        G[ny][nx] = "@"
        x, y = nx, ny
        pass
    elif nt in "[]":
        if dx != 0:
            # push horizontally
            _x, _y = nx, ny
            while True:
                _x, _y = _x + dx, _y + dy
                _t = G[_y][_x]
                if _t == "#":
                    break
                elif _t == ".":
                    for xx in range(_x, nx, -dx):
                        G[_y][xx] = G[_y][xx - dx]
                    G[ny][nx] = "@"
                    G[y][x] = "."
                    x, y = nx, ny
                    break
        else:
            # push vertically
            boxes = [(x, y)]
            box_layers = []
            try:
                while True:
                    new_boxes = set()
                    for bx, by in boxes:
                        nbx, nby = bx + dx, by + dy
                        t = G[nby][nbx]
                        if t == "#":
                            raise "not possible to move"
                        elif t == "[":
                            new_boxes.update([(nbx, nby), (nbx + 1, nby)])
                        elif t == "]":
                            new_boxes.update([(nbx, nby), (nbx - 1, nby)])
                    boxes = new_boxes
                    if len(new_boxes) == 0:
                        for layer in reversed(box_layers):
                            for bx, by in layer:
                                G[by + dy][bx] = G[by][bx]
                                G[by][bx] = "."
                        G[ny][nx] = "@"
                        G[y][x] = "."
                        x, y = nx, ny
                        break
                    else:
                        box_layers.append(deepcopy(new_boxes))

            except:
                pass
    # for r in G:
    #     print("".join(r))

# print("end")
# for r in G:
#     print("".join(r))


# calculate GPS
total = 0
for y in range(h):
    for x in range(w):
        if G[y][x] == "[":
            total += y * 100 + x

print(f"Part 2 answer: {total}")
# ----------part 2
