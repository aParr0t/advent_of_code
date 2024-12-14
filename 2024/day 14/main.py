# ----------common for both parts
from copy import deepcopy

inp = [s.strip("\n") for s in open("input.txt")]
robots_inp = []
for s in inp:
    p = eval(s[s.index("=") + 1 : s.index(" ")])
    v = eval(s[s.rindex("=") + 1 :])
    robots_inp.append([p, v])
# ----------common for both parts

# ----------part 1
w, h = 101, 103
robots = deepcopy(robots_inp)
for _ in range(100):
    for i, (p, v) in enumerate(robots):
        x, y = p
        x += v[0]
        y += v[1]
        x %= w
        y %= h
        robots[i][0] = (x, y)

Q = [0, 0, 0, 0]
qw, qh = w // 2, h // 2
for p, v in robots:
    x, y = p
    if x == qw or y == qh:
        continue
    if x > qw:
        x -= 1
    if y > qh:
        y -= 1
    qi = 2 * (y // qh) + x // qw
    Q[qi] += 1

answer = 1
for x in Q:
    answer *= x

print(f"Part 1 answer: {answer}")
# ----------part 1

# ----------part 2
# for part 2 I printed the whole grid after each second to see if i could see any pattern.
# i noticed the first ish patterns on round 77 (0-start) and 108.
# after that the next patterns cycled in fixed steps of 103 and 101.
# Then, intensely watching as the states got printed where the round matched
# either of those two patterns, finally I saw the christmas tree for a split second.
w, h = 101, 103
robots = deepcopy(robots_inp)
# these are the rounds when the patterns started showing
# 77,
# 108,
# 180,
# 209,
# 283,
# 310,
# 386,
# 411,
# 489,
# 512,
# 592,
# 613,
for round in range(0, 100001):
    # input()

    for i, (p, v) in enumerate(robots):
        x, y = p
        x += v[0]
        y += v[1]
        x %= w
        y %= h
        robots[i][0] = (x, y)

    # if (round - 77) % 103 == 0 or (round - 108) % 101 == 0:
    if round == 6875:
        # print(f"round: {round}")
        G = [[" " for x in range(w)] for y in range(h)]
        for p, v in robots:
            G[p[1]][p[0]] = "#"
        print()
        for r in G:
            print("".join(r))
        break


print(f"Part 2 answer: {6875+1}")
# ----------part 2
