# read input
inp = [s.rstrip() for s in open("input.txt")]

# parse history
H = [[] for l in inp]
for i, l in enumerate(inp):
    H[i].append([int(x) for x in l.split()])


# calculate difference until it is all zeroes
for i in range(len(H)):
    h_idx = 0
    while True:
        h = H[i][h_idx]
        diff = [h[j + 1] - h[j] for j in range(len(h) - 1)]
        H[i].append(diff)
        if all([x == 0 for x in diff]):
            break
        h_idx += 1

# ----------part 1
res = 0
for i in range(len(H)):
    pred = 0
    for j in range(len(H[i]) - 2, -1, -1):
        pred = pred + H[i][j][-1]
    res += pred

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
res = 0
for i in range(len(H)):
    pred = 0
    for j in range(len(H[i]) - 2, -1, -1):
        pred = H[i][j][0] - pred
    res += pred

print(f"Part 2 answer: {res}")
# ----------part 2
