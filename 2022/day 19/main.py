# read input
blueprints = []
for l in open("input.txt").readlines():
    l = l.rstrip("\n").replace(".", "")
    arr = l.split("Each")[1:]
    blueprint = {}
    for s in arr:
        s = s.strip()
        name = s[: s.index(" ")]
        blueprint[name] = {}
        costs = s.split("costs ")[1].split(" and ")
        for cost in costs:
            amount = int(cost[: cost.index(" ")])
            material = cost[cost.index(" ") + 1 :]
            blueprint[name][material] = amount
    blueprints.append(blueprint)


# ----------both parts

# ----------both parts

# ----------part 1

# print(f"Part 1 answer: {}")
# ----------part 1

# ----------part 2

# print(f"Part 2 answer: {}")
# ----------part 2
