# ----------common for both parts
import itertools

inp = [s.strip("\n") for s in open("input.txt")]
Q = []
for s in inp:
    test = int(s[: s.index(":")])
    nums = [int(x) for x in s[s.index(":") + 2 :].split(" ")]
    Q.append((test, nums))
# ----------common for both parts

# ----------part 1
total = 0
for test, nums in Q:
    n = len(nums) - 1
    for i in range(1 << n):
        # get binary representation of i, left padded with 0
        b = f"{bin(i)[2:]:}"
        b = "0" * (n - len(b)) + b
        # go through the bitset and calculate equation
        res = nums[0]
        for j in range(1, len(nums)):
            # 0 = +,    1 = *
            if b[j - 1] == "0":
                res += nums[j]
            elif b[j - 1] == "1":
                res *= nums[j]

        if res == test:
            total += test
            break

print(f"Part 1 answer: {total}")
# ----------part 1

# ----------part 2
total = 0
for test, nums in Q:
    n = len(nums) - 1
    combinations = itertools.product(["+", "*", "||"], repeat=n)
    for c in combinations:
        res = nums[0]
        for i in range(n):
            match c[i]:
                case "+":
                    res += nums[i + 1]
                case "*":
                    res *= nums[i + 1]
                case "||":
                    res = int(str(res) + str(nums[i + 1]))

        if res == test:
            total += test
            break

print(f"Part 2 answer: {total}")
# ----------part 2
