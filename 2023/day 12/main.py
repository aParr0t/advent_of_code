import functools

# read input
inp = [s.rstrip() for s in open("input.txt")]


# ----------part 1
# part 1 knocked me out. I used all my brain cells from 8 in the morning
# to 7 in the evening. Solved it while working out. "Genius" me thought that
# adding code to check if the answer was to low, based on previous wrong
# answers. I read the message wrong and thought that my answer was too low...

RO: list[str] = []
RE: list[list[int]] = []
for l in inp:
    ro, re = l.split()
    RO.append(ro)
    RE.append([int(x) for x in re.split(",")])

# an array for the valid strings. Helped me a ton for debugging
strings = []


def run(s: str, re: list[int], _start: int):
    if not re:
        if "#" in s[_start:]:
            return 0
        ns = s.replace("?", ".")
        strings.append(ns)
        return 1

    start = _start
    while start < len(s) and s[start] == ".":
        start += 1

    c = 0
    w = re[0]
    for i in range(start, len(s) - w + 1):
        if i >= 1 and s[i - 1] == "#":
            break
        if i == ".":
            continue
        d = 0
        for j in range(i, i + w):
            if s[j] != ".":
                d += 1

        if j < len(s) - 1 and s[j + 1] == "#":
            continue
        if d != w:
            continue

        ns = list(s)
        ns[i : j + 1] = "#" * w
        ns = "".join(ns)
        ns = ns[: j + 1].replace("?", ".") + ns[j + 1 :]
        c += run(ns, re[1:], j + 2)
    return c


res = 0
for ro, re in zip(RO, RE):
    c = run(ro, re, 0)
    res += c

print(f"Part 1 answer: {res}")

# these fking "smart" checks fked me up for several hours, answer was 7407
# if res <= 7564:
#     print("too low")
# if res >= 8223:
#     print("too high")
# if res in [8139, 7807, 8132]:
#     print("incorrect")
# ----------part 1


# ----------part 2
# For this day i had to use caching because the inputs got a loooot larger. I
# also saw that the function calls were repeated. To cache the function I had
# to convert one of the list-arguments to a string.

RO: list[str] = []
RE: list[str] = []
for l in inp:
    ro, re = l.split()
    ro = "?".join([ro for _ in range(5)])
    RO.append(ro)
    re = ",".join([re for _ in range(5)])
    RE.append(re)


# caching is my city
@functools.cache
def run(s: str, re: str, _start: int):
    if not re:
        if "#" in s[_start:]:
            return 0
        return 1

    start = _start
    while start < len(s) and s[start] == ".":
        start += 1

    c = 0
    w = re[0]

    re_split = re.find(",")
    if re_split != -1:
        w = int(re[:re_split])
    else:
        w = int(re)

    for i in range(start, len(s) - w + 1):
        if i >= 1 and s[i - 1] == "#":
            break
        if i == ".":
            continue
        for j in range(i, i + w):
            if s[j] == ".":
                break
        else:
            if j < len(s) - 1 and s[j + 1] == "#":
                continue

            if re_split == -1:
                c += run(s, "", j + 2)
            else:
                c += run(s, re[re_split + 1 :], j + 2)
    return c


res = 0
for ro, re in zip(RO, RE):
    c = run(ro, re, 0)
    res += c


print(f"Part 2 answer: {res}")
# ----------part 2
