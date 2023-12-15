# read input
IN = open("input.txt").read().rstrip().split(",")


def hsh(s: str):
    cur = 0
    for c in s:
        asc = ord(c)
        cur += asc
        cur *= 17
        cur %= 256
    return cur


# ----------part 1
res = 0
for com in IN:
    res += hsh(com)

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
B = [dict() for _ in range(256)]
for com in IN:
    if "=" in com:
        l, focal = com.split("=")
        focal = int(focal)
        idx = hsh(l)
        B[idx][l] = focal
    else:
        l = com[:-1]
        idx = hsh(l)
        if l in B[idx]:
            B[idx].pop(l)

res = 0
for b_idx, b in enumerate(B):
    for l_idx, focal in enumerate(b.values()):
        power = (b_idx + 1) * (l_idx + 1) * focal
        res += power

print(f"Part 2 answer: {res}")
# ----------part 2
