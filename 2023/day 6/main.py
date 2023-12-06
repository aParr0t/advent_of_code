# read input
inp = [s.rstrip() for s in open("input.txt")]

# ----------part 1
times = [int(l) for l in inp[0].split("Time: ")[1].split(" ") if l]
distances = [int(l) for l in inp[1].split("Distance: ")[1].split(" ") if l]

A = []
res = 1
for t, d in zip(times, distances):
    half = t / 2
    DS = []
    for t0 in range(1, int(round(half)) + 1):
        d0 = (t - t0) * t0
        if d0 > d:
            DS.append(d0)

    if t % 2 == 1:
        mul = len(DS) * 2 - 2
    else:
        mul = (len(DS) - 1) * 2 + 1
    res *= mul

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
t = int(inp[0].split("Time:")[1].replace(" ", ""))
d = int(inp[1].split("Distance:")[1].replace(" ", ""))

lowest = 0
for t0 in range(1, t + 1):
    d0 = (t - t0) * t0
    if d0 > d:
        lowest = t0
        break

res = t - 2 * lowest + 1

print(f"Part 2 answer: {res}")
# ----------part 2
