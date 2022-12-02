import itertools
from collections import Counter, defaultdict

# read input
inp = [s.rstrip() for s in open("input.txt")]
rounds = [s.split(" ") for s in inp]

# ---------- both parts
choice_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
# ---------- both parts

# ----------part 1
# A, X = rock
# B, Y = paper
# C, Z = scissors
# states = {
#     "A": {"X": 1, "Y": 2, "Z": 0},
#     "B": {"X": 0, "Y": 1, "Z": 2},
#     "C": {"X": 2, "Y": 0, "Z": 1},
# }

# total_score = 0
# outcome_step = 3
# for [opponent, player] in rounds:
#     total_score += states[opponent][player] * outcome_step
#     total_score += choice_points[player]

# print(f"Part 1 answer: {total_score}")
# ----------part 1

# ----------part 2
# A, X = rock
# B, Y = paper
# C, Z = scissors
# X = loose
# Y = draw
# Z = win
states = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"},
}
round_points = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

total_score = 0
for [opponent, end_state] in rounds:
    player = states[opponent][end_state]
    total_score += round_points[end_state]
    total_score += choice_points[player]

print(f"Part 2 answer: {total_score}")
# ----------part 2
