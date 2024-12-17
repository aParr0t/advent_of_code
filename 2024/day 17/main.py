# ----------common for both parts
inp = [s.strip("\n") for s in open("input.txt")]
reg_inp = list(map(int, [s[s.rindex(" ") + 1 :] for s in inp[:3]]))
program = [int(x) for x in inp[-1].split(" ")[-1].split(",")]


def combo(op: int, regs):
    if 0 <= op <= 3:
        return op
    if 4 <= op <= 6:
        return regs[op - 4]
    if op == 7:
        print("7 is not in a valid program")


def run(regs, program):
    a, b, c = regs
    pointer = 0
    std_out = []
    while pointer < len(program):
        op = program[pointer + 1]
        match program[pointer]:
            case 0:
                # adv
                a = a >> combo(op, (a, b, c))
            case 1:
                # bxl
                b ^= op
            case 2:
                # bst
                b = combo(op, (a, b, c)) % 8
            case 3:
                # jnz
                if a == 0:
                    pass
                else:
                    pointer = op - 2
            case 4:
                # bxc
                b ^= c
            case 5:
                # out
                std_out.append(combo(op, (a, b, c)) % 8)
            case 6:
                # bdv
                b = a >> combo(op, (a, b, c))
            case 7:
                # bdv
                c = a >> combo(op, (a, b, c))
        pointer += 2
    return std_out


# ----------common for both parts


# ----------part 1
answer1 = ",".join([str(x) for x in run(reg_inp, program)])
print(f"Part 1 answer: {answer1}")
# ----------part 1


# ----------part 2
def spot_pattern():
    """
    I used the code inside of this function to spot the pattern in this task
    """
    for a in range(1000):
        _, b, c = reg_inp
        run_program = run((a, b, c), program)
        run_program = [0] * (len(program) - len(run_program)) + run_program
        print(",".join([str(x) for x in run_program]))


i = len(program) - 1
answer2 = 8**i
run_program = run((answer2, 0, 0), program)
while run_program != program:
    run_program = run((answer2, 0, 0), program)
    run_program += [0] * (len(program) - len(run_program))
    if run_program[i] == program[i]:
        i -= 1
    else:
        answer2 += 8**i

print(f"Part 2 answer: {answer2}")
# ----------part 2
