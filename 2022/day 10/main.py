# read input
program = [s.rstrip("\n") for s in open("input.txt")]

# ----------both parts

# ----------both parts

# ----------part 1
def cycle():
    global cycle_count, strength_sum

    # during cycle
    if (cycle_count - 20) % 40 == 0:
        signal_strength = cycle_count * register
        strength_sum += signal_strength

    # ending cycle
    cycle_count += 1


strength_sum = 0
register = 1
cycle_count = 1
for instruction in program:
    if instruction == "noop":
        cycle()
    elif instruction.startswith("addx"):
        cycle()
        cycle()
        add_value = int(instruction[5:])
        register += add_value


print(f"Part 1 answer: {strength_sum}")
# ----------part 1

# ----------part 2
def cycle():
    global cycle_count, screen

    pixel_idx = cycle_count - 1
    isSpriteVisible = abs(register - (pixel_idx % screen_w)) < 2
    if isSpriteVisible:
        screen[pixel_idx] = "#"

    # ending cycle
    cycle_count += 1


screen_w, screen_h = 40, 6
screen = ["." for _ in range(screen_w * screen_h)]
register = 1
cycle_count = 1
for instruction in program:
    if instruction == "noop":
        cycle()
    elif instruction.startswith("addx"):
        cycle()
        cycle()
        add_value = int(instruction[5:])
        register += add_value

# draw screen
for idx in range(0, screen_w * screen_h, screen_w):
    print("".join(screen[idx : idx + screen_w]))

print(f"Part 2 answer: RZHFGJCB")
# ----------part 2
