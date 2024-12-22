# ----------common for both parts
from collections import defaultdict

init_secrets = [s.strip("\n") for s in open("input.txt")]
init_secrets = list(map(int, init_secrets))


def mix(a: int, b: int):
    return a ^ b


def prune(s: int):
    return s % 16777216


def next_secret(s: int):
    # first
    res = s * 64
    s = mix(res, s)
    s = prune(s)
    # second
    res = s // 32
    s = mix(res, s)
    s = prune(s)
    # third
    res = s * 2048
    s = mix(res, s)
    s = prune(s)
    return s


# ----------common for both parts


# ----------part 1
finals = []
for init_secret in init_secrets:
    s = init_secret
    for i in range(2000):
        s = next_secret(s)
    finals.append(s)
answer1 = sum((finals))

print(f"Part 1 answer: {answer1}")
# ----------part 1

# ----------part 2
all_rel_changes = []
all_bananas = []
for init_secret in init_secrets:
    rel_changes = [-11] * 2001
    bananas = [99] * 2001
    s = init_secret
    bananas[0] = s % 10
    for i in range(1, 2001):
        s = next_secret(s)
        bananas[i] = s % 10
        rel_changes[i] = bananas[i] - bananas[i - 1]
    all_bananas.append(bananas)
    all_rel_changes.append(rel_changes)

merged_first = defaultdict(int)
for bananas, rel_changes in zip(all_bananas, all_rel_changes):
    first = {}
    for i in range(1, len(rel_changes) - 3):
        t = tuple(rel_changes[i : i + 4])
        if t in first:
            continue
        first[t] = bananas[i + 3]

    for k, v in first.items():
        merged_first[k] += v

best_pair = max(merged_first.items(), key=lambda x: x[1])
answer2 = best_pair[1]

print(f"Part 2 answer: {answer2}")
# ----------part 2
