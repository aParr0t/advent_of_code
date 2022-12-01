# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

class Command:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Part One
# convert strings into commands and arguments
commands = [Command(x[:3], int(x[4:])) for x in puzzleInput]
tried = set()
pointer, accumulator = 0, 0
while True:
    # add the index of this command to set if it is the first time executing this command
    if pointer not in tried:
        tried.add(pointer)
    else:
        # index is the answer if it is the second time executing this command
        print("Part One answer : " + str(accumulator))
        break

    # execute the commands
    instruction = commands[pointer]
    if instruction.name == "acc":
        accumulator += instruction.value
        pointer += 1
    elif instruction.name == "nop":
        pointer += 1
    elif instruction.name == "jmp":
        pointer += instruction.value
# Part One



# Part Two
def testIfTerminates():
    tried = set()
    pointer, accumulator = 0, 0
    
    # executes commands until visits one command for the second time
    # the answer is the accumulator if it reaches the end of the command list
    while True:
        if pointer not in tried:
            tried.add(pointer)
        else:
            return False, False

        instruction = commands[pointer]
        if instruction.name == "acc":
            accumulator += instruction.value
            pointer += 1
        elif instruction.name == "nop":
            pointer += 1
        elif instruction.name == "jmp":
            pointer += instruction.value

        # answer is found if it reached the end
        if pointer >= len(commands):
            return True, accumulator


commands = [Command(x[:3], int(x[4:])) for x in puzzleInput]
# brute force the sollution with changing every jmp to nop and every nop to jump
for line in commands:
    if line.name == "acc":
        continue
    # change jmp to nop. If not terminated, then set the nop back to jmp
    elif line.name == "jmp":
        line.name = "nop"
        terminated, accumulator = testIfTerminates()
        if terminated:
            print("Part Two answer : " + str(accumulator))
            break
        else:
            line.name = "jmp"
    # change nop to jmp. If not terminated, then set the jmp back to nop
    elif line.name == "nop":
        line.name = "jmp"
        terminated, accumulator = testIfTerminates()
        if terminated:
            print("Part Two answer : " + str(accumulator))
            break
        else:
            line.name = "nop"
# Part Two