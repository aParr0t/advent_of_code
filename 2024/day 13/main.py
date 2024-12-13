# ----------common for both parts
import math

inp = [s.strip("\n") for s in open("input.txt")]
machines = []
for m in "@".join(inp).split("@@"):
    a = (
        int(m[m.index("X+") + 2 : m.index(",")]),
        int(m[m.index("Y+") + 2 : m.index("@")]),
    )
    bidx = m.index("B:")
    b = (
        int(m[bidx + 5 : m.index(",", bidx)]),
        int(m[m.index("Y", bidx) + 2 : m.index("@", bidx)]),
    )
    pidx = m.index("Prize:")
    p = (
        int(m[pidx + 9 : m.index(",", pidx)]),
        int(m[m.index("Y", pidx) + 2 :]),
    )
    machines.append((a, b, p))


def solve_2x2(A: list, b: list):
    """
    Solves Ax=b using elementary row operations.
    This implementation tries to avoid float numbers until the very end.
    """
    A = A.copy()
    A[0].append(b[0])
    A[1].append(b[1])
    w, h = len(A[0]), len(A)

    # row operations
    # make column 1 equal
    l = math.lcm(A[0][0], A[1][0])
    for y in range(h):
        mul = l // A[y][0]
        for x in range(w):
            A[y][x] *= mul

    # subtract row 0 from row 1
    for i in range(w):
        A[1][i] -= A[0][i]

    # make column 2 equal
    l = math.lcm(A[0][1], A[1][1])
    for y in range(h):
        mul = l // A[y][1]
        for x in range(w):
            A[y][x] *= mul

    # subtract row 1 from row 0
    for i in range(w):
        A[0][i] -= A[1][i]

    # solve
    c_a = A[0][2] / A[0][0]
    c_b = A[1][2] / A[1][1]
    return c_a, c_b


# ----------common for both parts

# ----------part 1
presses = 0
for m in machines:
    a, b, p = m
    A = [[a[0], b[0]], [a[1], b[1]]]
    c_a, c_b = solve_2x2(A, p)
    is_a_decimal = c_a != int(c_a)
    is_b_decimal = c_b != int(c_b)
    if is_a_decimal or is_b_decimal:
        continue
    c_a, c_b = int(c_a), int(c_b)
    presses += c_a * 3 + c_b * 1

print(f"Part 1 answer: {presses}")
# ----------part 1

# ----------part 2
presses = 0
for m in machines:
    a, b, p = m
    p = [x + 10000000000000 for x in p]
    A = [[a[0], b[0]], [a[1], b[1]]]
    c_a, c_b = solve_2x2(A, p)
    is_a_decimal = c_a != int(c_a)
    is_b_decimal = c_b != int(c_b)
    if is_a_decimal or is_b_decimal:
        continue
    c_a, c_b = int(c_a), int(c_b)
    presses += c_a * 3 + c_b * 1

print(f"Part 2 answer: {presses}")
# ----------part 2
