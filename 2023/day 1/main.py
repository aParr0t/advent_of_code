# read input
inp = [s.rstrip() for s in open("input.txt")]

# ----------part 1
res = 0
for s in inp:
    nums = [x for x in s if x.isdigit()]
    num = int(nums[0] + nums[-1])
    res += num

print(f"Part 1 answer: {res}")
# ----------part 1

# ----------part 2
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

res = 0
for s in inp:
    # find first digit
    first = ""
    last = ""
    for i in range(len(s)):
        ss = s[i:]
        if ss[0].isdigit():
            if not first:
                first = int(ss[0])
            last = ss[0]
            continue
        for num, string_num in enumerate(numbers, 1):
            if ss.startswith(string_num):
                if not first:
                    first = num
                last = num
                break

    res += int(f"{first}{last}")

print(f"Part 2 answer: {res}")
# ----------part 2
