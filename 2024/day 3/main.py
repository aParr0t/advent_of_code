# ----------common for both parts
inp = open("input.txt").read()
# ----------common for both parts

# ----------part 1
result = 0
for slice in inp.split("mul("):
    try:
        i = 0
        # find a
        while True and i < len(slice):
            if slice[i] == ",":
                break
            i += 1
        a = int(slice[:i])
        i += 1
        # find b
        b_start = i
        while True and i < len(slice):
            if slice[i] == ")":
                break
            i += 1
        b = int(slice[b_start:i])
        # multiply
        result += a * b
    except:
        continue

print(f"Part 1 answer: {result}")
# ----------part 1

# ----------part 2
result = 0
enabled = True
for i in range(len(inp)):
    s = inp[i:]
    if s.startswith("do()"):
        enabled = True
    elif s.startswith("don't()"):
        enabled = False
    elif s.startswith("mul(") and enabled:
        # same as in part 1
        try:
            a_start = j = len("mul(")
            while True and j < len(s):
                if s[j] == ",":
                    break
                j += 1
            a = int(s[a_start:j])
            j += 1
            b_start = j
            while True and j < len(s):
                if s[j] == ")":
                    break
                j += 1
            b = int(s[b_start:j])
            result += a * b
        except:
            continue


print(f"Part 2 answer: {result}")
# ----------part 2
