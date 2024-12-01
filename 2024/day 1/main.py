from collections import defaultdict

# ----------common for both parts
inp = [s.rstrip("\n") for s in open("input.txt")]
left, right = [], []
for s in inp:
    l, *_, r = s.split(" ")
    left.append(int(l))
    right.append(int(r))
# ----------common for both parts

# ----------part 1
left.sort()
right.sort()
total_distance = 0
for i in range(len(left)):
    total_distance += abs(left[i] - right[i])

print(f"Part 1 answer: {total_distance}")
# ----------part 1

# ----------part 2
counts = defaultdict(int)
for v in right:
    counts[v] += 1

similarity_score = 0
for v in left:
    similarity_score += v * counts[v]

print(f"Part 2 answer: {similarity_score}")
# ----------part 2
