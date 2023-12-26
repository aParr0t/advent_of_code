from collections import deque
from copy import deepcopy

# read input
IN = [s.rstrip() for s in open("input.txt")]

w, h = len(IN[0]), len(IN)

s = ()

for y in range(h):
    for x in range(w):
        if IN[y][x] == "S":
            s = (x, y)


D = {}
Q = deque()
Q.append(s)
D[s] = 0
d = 0
while Q:
    NQ = deque()
    d += 1
    while Q:
        x, y = Q.popleft()
        for n in [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1),
        ]:
            if n in D or not (0 <= n[0] < w) or not (0 <= n[1] < h):
                continue
            if IN[n[1]][n[0]] == "#":
                continue

            NQ.append(n)
            D[n] = d
    Q = NQ

# ----------part 1
# Did part 1 on my own. Pretty easy
res = 0
for y in range(h):
    for x in range(w):
        if (x, y) in D:
            d = D[(x, y)]
            if d % 2 == 0 and d <= 64:
                res += 1

print(f"Part 1 answer: {res}")  # 3858
# ----------part 1


# ----------part 2
# Part 2 was a nightmare. I then observed that the middle row and column was
# empty of rocks. This allowed the elf to travel in all four directions as far
# as possible. I then drew a diagram of a diamond which showed what tiles were
# inside the reachable area. I noticed that the tiles on the edge were cut of
# and that corners needed to be considered. I took a dumb assumption that
# opposite corners would even each other out. Dumb, dumb, dumb. But I was very
# close. I have attached an image of how far I had come. To finish it of, I had
# to get help from reddit: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
odd = 0
even = 0
odd_corner = 0
even_corner = 0
for y in range(h):
    for x in range(w):
        if (x, y) in D:
            d = D[(x, y)]
            if d % 2 == 0:
                even += 1
                if d > 65:
                    even_corner += 1
            else:
                odd += 1
                if d > 65:
                    odd_corner += 1


steps = 26_501_365
steps_side = int(steps - ((w - 1) / 2))
n = int(steps_side / w)

even_boards = 0
odd_boards = 1
is_even_board = False
for i in range(1, n + 1):
    is_even_board = not is_even_board
    if is_even_board:
        even_boards += i * 4
    else:
        odd_boards += i * 4

assert (n + 1) ** 2 == odd_boards
assert n**2 == even_boards

res = even_boards * even + odd_boards * odd
if is_even_board:
    res -= (n + 1) * even_corner
    res += n * odd_corner
else:
    res += n * even_corner
    res -= (n + 1) * odd_corner


print(f"Part 2 answer: {res}")

if res <= 635900299361343:
    print("your answer is too low")
if res in [10920357014155013343, 636350477551343, 636352044956109, 636352044971647]:
    print("That's not the right answer")
# ----------part 2
