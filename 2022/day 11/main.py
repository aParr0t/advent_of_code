# read input
inp = [s.strip().replace(",", "") for s in open("input.txt")]


# ----------both parts
monkeys = {}
monkey_num = 0
for s in inp:
    tokens = s.split(" ")
    if s.startswith("Monkey"):
        monkey = {"inspected_count": 0}
    elif s.startswith("Starting"):
        monkey["items"] = [int(x) for x in tokens[2:]]
    elif s.startswith("Operation"):
        monkey["operator"] = tokens[-2]
        monkey["operand"] = tokens[-1]
    elif s.startswith("Test"):
        monkey["divisor"] = int(tokens[-1])
    elif s.startswith("If true"):
        monkey["true_monkey"] = int(tokens[-1])
    elif s.startswith("If false"):
        monkey["false_monkey"] = int(tokens[-1])
    elif s == "":
        monkeys[monkey_num] = monkey
        monkey_num += 1
monkeys[monkey_num] = monkey

# ----------both parts

# ----------part 1
for round in range(20):
    for monkey in monkeys.values():
        monkey["inspected_count"] += len(monkey["items"])
        for item in monkey["items"]:
            # inspect
            if monkey["operand"] == "old":
                operand = item
            else:
                operand = int(monkey["operand"])

            if monkey["operator"] == "+":
                inspected_item = item + operand
            elif monkey["operator"] == "*":
                inspected_item = item * operand

            # get bored
            inspected_item //= 3

            # test
            if inspected_item % monkey["divisor"] == 0:
                to_monkey = monkeys[monkey["true_monkey"]]
            else:
                to_monkey = monkeys[monkey["false_monkey"]]

            # throw
            to_monkey["items"].append(inspected_item)

        # remove thrown items
        monkey["items"] = []

active_monkeys = [m["inspected_count"] for m in monkeys.values()]
active_monkeys.sort()
monkey_business = active_monkeys[-1] * active_monkeys[-2]

print(f"Part 1 answer: {monkey_business}")
# ----------part 1

# ----------part 2
lcm = 1  # least common multiple
for monkey in monkeys.values():
    lcm *= monkey["divisor"]

for round in range(10000):
    for monkey in monkeys.values():
        monkey["inspected_count"] += len(monkey["items"])
        for item in monkey["items"]:
            # inspect
            if monkey["operand"] == "old":
                operand = item
            else:
                operand = int(monkey["operand"])

            if monkey["operator"] == "+":
                inspected_item = item + operand
            elif monkey["operator"] == "*":
                inspected_item = item * operand

            inspected_item %= lcm

            # test
            if inspected_item % monkey["divisor"] == 0:
                to_monkey = monkeys[monkey["true_monkey"]]
            else:
                to_monkey = monkeys[monkey["false_monkey"]]

            # throw
            to_monkey["items"].append(inspected_item)

        # remove thrown items
        monkey["items"] = []

active_monkeys = [m["inspected_count"] for m in monkeys.values()]
active_monkeys.sort()
monkey_business = active_monkeys[-1] * active_monkeys[-2]

print(f"Part 2 answer: {monkey_business}")
# ----------part 2
