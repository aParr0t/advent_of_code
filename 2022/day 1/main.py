# read input
inp = [s.rstrip() for s in open("input.txt")]
inp = [int(x) if x else "" for x in inp]

# ----------part 1
# max_num = 0
# num = 0
# for i in range(len(inp) + 1):
#     if i == len(inp) or inp[i] == "":
#         max_num = max(num, max_num)
#         num = 0
#     else:
#         num += inp[i]

# print(f"Part 1 answer: {max_num}")
# ----------part 1

# ----------part 2
num = 0
best = []
for i in range(len(inp) + 1):
    if i == len(inp) or inp[i] == "":
        if len(best) == 0:
            best.append(num)
        else:
            for insert_idx in range(len(best)):
                if num > best[insert_idx]:
                    best.insert(insert_idx, num)
                    if len(best) == 3 + 1:
                        del best[-1]
                    break
        num = 0
    else:
        num += inp[i]

print(f"Part 2 answer: {sum(best)}")
# ----------part 2
