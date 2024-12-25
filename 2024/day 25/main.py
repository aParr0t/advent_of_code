# ----------common for both parts
inp = [s.strip("\n") for s in open("input.txt")]
inp.append("")
keys, locks = [], []
for i in range(0, len(inp), 8):
    p = inp[i : i + 7]
    # find heights
    heights = []
    for x in range(0, 5):
        h = 0
        for y in range(i + 1, i + 6):
            if inp[y][x] == "#":
                h += 1
        heights.append(h)
    heights = tuple(heights)
    if p[0][0] == "#":
        # lock
        locks.append(heights)
    else:
        keys.append(heights)
# ----------common for both parts

# ----------part 1
total = 0
for l in locks:
    for k in keys:
        for lh, kh in zip(l, k):
            if kh + lh > 5:
                break
        else:
            total += 1

print(f"Part 1 answer: {total}")
# ----------part 1
