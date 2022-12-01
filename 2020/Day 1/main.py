# read the input
inputFile = open("input.txt", "r")
nums = inputFile.readlines()

for i in range(len(nums)):
    nums[i] = int(nums[i].rstrip("\n"))


#Part One
for num in nums:
    rest = 2020-num
    if rest in nums:
        answer = num * nums[nums.index(rest)]

print(answer)
# Part One


# Part Two
rests = []
for i in range(len(nums)):
    rests.append(2020-nums[i])

answer = False
for rest in rests:
    for num in nums:
        rest2 = rest-num
        if rest2 in nums:
            answer = nums[rests.index(rest)] * num * rest2
            break
    if answer:
        break
print(answer)
# Part Two