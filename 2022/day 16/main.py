# looked for help for part 1. Didn't understand the solutions for part 2

# read input
inp = [s.rstrip("\n").replace(",", "").split(" ") for s in open("input.txt")]

valves = {}
for tokens in inp:
    valve_name = tokens[1]
    flow_rate = int(tokens[4][5:-1])
    tunnels = tokens[9:]
    valves[valve_name] = {"flow_rate": flow_rate, "tunnels": tunnels}

# ----------both parts

# ----------both parts

# ----------part 1
def pressure_sum(valve_codes):
    total = 0
    for valve_code in valve_codes:
        total += valves[valve_code]["flow_rate"]
    return total


mem = {}


def search(valve, pressure, time_left, opened_valves):
    if time_left == 0:
        return pressure

    key = f"{valve}-{pressure}-{time_left}-{''.join(sorted(opened_valves))}"
    if key in mem:
        return mem[key]

    pressure += pressure_sum(opened_valves)
    ans = pressure

    time_left -= 1

    if valve not in opened_valves and valves[valve]["flow_rate"] > 0:
        ans = max(
            ans, search(valve, pressure, time_left, [*opened_valves, valve])
        )

    for tunnel in valves[valve]["tunnels"]:
        ans = max(ans, search(tunnel, pressure, time_left, opened_valves))

    mem[key] = ans
    return ans


best = search("AA", 0, 30, [])

print(f"Part 1 answer: {best}")
# ----------part 1

# ----------part 2

# print(f"Part 2 answer: {}")
# ----------part 2
