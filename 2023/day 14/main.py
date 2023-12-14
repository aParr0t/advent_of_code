# read input
IN = [s.rstrip() for s in open("input.txt")]

w, h = len(IN[0]), len(IN)


def tilt(ar: list, dir: tuple):
    if dir[0] == 0:
        # vertical tilt
        if dir[1] == 1:
            ar.reverse()
        for y in range(h):
            for x in range(w):
                if ar[y][x] != "O":
                    continue

                for y2 in range(y - 1, -1, -1):
                    is_edge = y2 == 0 and ar[0][x] == "."
                    if ar[y2][x] != "." or is_edge:
                        if is_edge:
                            y2 = -1

                        s = ar[y]
                        ar[y] = s[:x] + "." + s[x + 1 :]
                        s = ar[y2 + 1]
                        ar[y2 + 1] = s[:x] + "O" + s[x + 1 :]
                        break
        if dir[1] == 1:
            ar.reverse()
    else:
        # horizontal tilt
        if dir[0] == 1:
            ar = [s[::-1] for s in ar]
        for x in range(w):
            for y in range(h):
                if ar[y][x] != "O":
                    continue
                for x2 in range(x - 1, -1, -1):
                    is_edge = x2 == 0 and ar[y][x2] == "."
                    if ar[y][x2] != "." or is_edge:
                        if is_edge:
                            x2 = -1

                        s = list(ar[y])
                        s[x] = "."
                        s[x2 + 1] = "O"
                        ar[y] = "".join(s)
                        break
        if dir[0] == 1:
            ar = [s[::-1] for s in ar]
    return ar


def load(ar: list):
    l = 0
    for i, r in enumerate(ar):
        l += r.count("O") * (h - i)
    return l


# ----------part 1
T = tilt([*IN], (0, -1))
res = load(T)

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
def cycle(ar: list):
    ar = tilt(ar, (0, -1))
    ar = tilt(ar, (-1, 0))
    ar = tilt(ar, (0, 1))
    ar = tilt(ar, (1, 0))
    return ar


T = IN
V = set()
V.add("".join(T))
loop = []
br_tup = None
for i in range(1, 10000):
    T = cycle(T)
    hsh = "".join(T)
    if hsh in V:
        tup = (hsh, load(T))
        if not br_tup:
            br_tup = tup
            stub = i
        elif br_tup == tup:
            break
        loop.append(load(T))
    else:
        V.add(hsh)

loop_len = len(loop)
idx = (1000000000 - stub) % loop_len
res = loop[idx]

print(f"Part 2 answer: {res}")
# ----------part 2
