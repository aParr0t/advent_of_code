# ----------common for both parts
from collections import defaultdict

inp = [s.strip("\n") for s in open("input.txt")]

CON = defaultdict(list)
for s in inp:
    a, b = s.split("-")
    CON[a].append(b)
    CON[b].append(a)
# ----------common for both parts

# ----------part 1
triples = set()
for a, cons in CON.items():
    if not a.startswith("t"):
        continue
    for i, b in enumerate(cons):
        for c in CON[b]:
            if c in cons[i + 1 :]:
                triples.add(tuple(sorted((a, b, c))))

answer1 = len(triples)
print(f"Part 1 answer: {answer1}")
# ----------part 1

# ----------part 2
CON = defaultdict(set)
for s in inp:
    a, b = s.split("-")
    CON[a].add(b)
    CON[b].add(a)

comps = set()
for a, cons in CON.items():
    for i, b in enumerate(cons):
        for c in CON[b]:
            if c in cons:
                comps.add(tuple(sorted((a, b, c))))

comps = [set(c) for c in comps]
# print(f"Number of triples: {len(comps)}")
iteration = 0
while True:
    new_comps = set()
    iteration += 1
    # print()
    # print(f"iteration {iteration}")
    # print(f"number of comps: {len(comps)}")
    expanded = False

    # try to expand
    for comp in comps:
        for node in comp:
            for neighbor in CON[node]:
                # see if this neighbor can be added
                intersection = len(comp.intersection(CON[neighbor]))
                if intersection >= len(comp):
                    new_comp = tuple(sorted([*comp, neighbor]))
                    new_comps.add(new_comp)
                    expanded = True

    if expanded:
        comps = [set(c) for c in new_comps]
    else:
        break

best = max(comps, key=lambda x: len(x))
answer2 = ",".join(sorted(best))

print(f"Part 2 answer: {answer2}")
# ----------part 2
