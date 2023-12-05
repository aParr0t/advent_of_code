# read input
inp = [s.rstrip() for s in open("input.txt")]

w, h = len(inp[0]), len(inp)

# ----------part 1
# got the symbols with: print(set("".join(inp)))
symbols = [
    "%",
    "*",
    "-",
    "&",
    "/",
    "#",
    "+",
    "=",
    "$",
    "@",
]
symbol_set = set(symbols)


def is_part_number(line: int, start: int, end: int):
    for y in range(-1, 2):
        l = line + y
        if not (0 <= l < h):
            continue
        _start = max(start - 1, 0)
        _end = min(end + 1, w)
        window = inp[l][_start:_end]
        has_symbol = len(set(window).intersection(symbol_set))
        if has_symbol:
            return True
    return False


res = 0
for line_idx, l in enumerate(inp):
    i = 0
    while i < w:
        if l[i].isdigit():
            j = i
            while j < w and l[j].isdigit():
                j += 1
            is_part = is_part_number(line_idx, i, j)
            if is_part:
                res += int(l[i:j])
            i = j + 1
        else:
            i += 1

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
def get_number(y: int, x: int):
    l = inp[y]
    x1 = x
    while l[x1].isdigit():
        x1 -= 1
    x1 += 1  # start of number
    x2 = x
    while l[x2].isdigit():
        x2 += 1
    return int(l[x1:x2]), (x1, x2)


def gear_check(y: int, x: int):
    parts = {}
    for i in range(y - 1, y + 2):
        if not (0 <= i < h):
            continue
        for j in range(x - 1, x + 2):
            if not (0 <= j < w):
                continue
            if inp[i][j].isdigit():
                number, (start, end) = get_number(i, j)
                key = f"{i}-{start}-{end}"
                parts[key] = number

    if len(parts) == 2:
        parts = list(parts.values())
        return (True, parts[0] * parts[1])
    return (False, 0)


res = 0
for y, line in enumerate(inp):
    for x, c in enumerate(line):
        if c == "*":
            is_gear, gear_ratio = gear_check(y, x)
            if is_gear:
                res += gear_ratio


print(f"Part 2 answer: {res}")

# ----------part 2
