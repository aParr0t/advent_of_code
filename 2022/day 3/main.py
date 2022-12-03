# read input
inp = [s.rstrip() for s in open("input.txt")]

# ---------- both parts
def item_priority(item: str):
    item_unicode = ord(item)
    if 97 <= item_unicode <= 122:
        return item_unicode - 96
    elif 65 <= item_unicode <= 90:
        return item_unicode - 38


# ---------- both parts

# ----------part 1
priority_sum = 0
for rucksack in inp:
    ruck_len = len(rucksack)
    compartment_1 = rucksack[: ruck_len // 2]
    compartment_2 = rucksack[ruck_len // 2 :]

    wrong_item = set(compartment_1).intersection(set(compartment_2)).pop()
    priority_sum += item_priority(wrong_item)

print(f"Part 1 answer: {priority_sum}")
# ----------part 1

# ----------part 2
priority_sum = 0
for group_idx in range(0, len(inp), 3):
    uniques = set(inp[group_idx])
    for rucksack in inp[group_idx + 1 : group_idx + 3]:
        uniques = uniques.intersection(set(rucksack))

    wrong_item = uniques.pop()
    priority_sum += item_priority(wrong_item)

print(f"Part 2 answer: {priority_sum}")
# ----------part 2
