# read input
assignments = [
    s.rstrip().replace(",", "-").split("-") for s in open("input.txt")
]
assignments = [[int(x) for x in arr] for arr in assignments]

# ----------part 1
total_overlaps = 0
for assignment in assignments:
    pair1, pair2 = assignment[:2], assignment[2:]
    pair_1_overlaps_2 = pair2[0] <= pair1[0] and pair1[1] <= pair2[1]
    pair_2_overlaps_1 = pair1[0] <= pair2[0] and pair2[1] <= pair1[1]
    if pair_1_overlaps_2 or pair_2_overlaps_1:
        total_overlaps += 1

print(f"Part 1 answer: {total_overlaps}")
# ----------part 1

# ----------part 2
partial_overlaps = 0
for assignment in assignments:
    pair1, pair2 = assignment[:2], assignment[2:]
    left_not_overlap = pair1[1] < pair2[0]
    right_not_overlap = pair1[0] > pair2[1]
    if not (left_not_overlap or right_not_overlap):
        partial_overlaps += 1

print(f"Part 2 answer: {partial_overlaps}")
# ----------part 2
