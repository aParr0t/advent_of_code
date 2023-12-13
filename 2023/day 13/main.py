import functools

# read input
P = [s.split("\n") for s in open("input.txt").read().split("\n\n")]


# ----------part 1
# solved part one by checking rows and columns separately. When checking,
# I keep a reversed list of the visited rows/columns. Then at each
# new row/column I can check if the next rows/columns match the visited list.
# Some extra length checking for the lists is needed because the reflection
# doesn't need to be in the center of the pattern.

res = 0
for p in P:
    # check rows
    m = []
    for i, r in enumerate(p):
        m.insert(0, r)
        l = min(len(p) - i - 1, len(m))
        if i != len(p) - 1 and p[i + 1 : i + 1 + l] == m[:l]:
            res += 100 * (i + 1)
            break

    # check columns
    cols = []
    for i in range(len(p[0])):
        cols.append("".join([r[i] for r in p]))

    m = []
    for i in range(len(p[0])):
        m.insert(0, cols[i])
        l = min(len(p[0]) - i - 1, len(m))

        if i != len(cols) - 1 and cols[i + 1 : i + 1 + l] == m[:l]:
            res += i + 1
            break


print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# Part two seemed difficult at first, but was quite easy. The code does
# the exact same thing as in part 1, except that now it checks how many
# "smudges" there are. If the number of smudges is equal to one, then don't
# even bother correcting the smudge, just add the reflection-score
# to the result. Checking the number of smudges is just checking how many
# characters are different in the two reflections.


def diff(s1: str, s2: str):
    """Compares how many characters are different in the two strings. Compares index by index"""
    d = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            d += 1
    return d


res = 0
for p in P:
    # check rows
    m = []
    for i, r in enumerate(p):
        m.insert(0, r)
        l = min(len(p) - i - 1, len(m))
        s1, s2 = "".join(p[i + 1 : i + 1 + l]), "".join(m[:l])
        d = diff(s1, s2)
        if d == 1:
            res += 100 * (i + 1)
            break

    # create the columns
    cols = []
    for i in range(len(p[0])):
        cols.append("".join([r[i] for r in p]))

    # check columns
    m = []
    for i in range(len(p[0])):
        m.insert(0, cols[i])
        l = min(len(p[0]) - i - 1, len(m))
        s1, s2 = "".join(cols[i + 1 : i + 1 + l]), "".join(m[:l])
        d = diff(s1, s2)
        if d == 1:
            res += i + 1
            break


print(f"Part 2 answer: {res}")
# ----------part 2
