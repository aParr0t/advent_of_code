# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()

for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# Part One
groups = []
answers = ""
for line in puzzleInput:
    if line != "":
        # add the answers that the person answerd "yes" to, to the total
        answers += line
    elif line == "":
        # get only the unique answers from the list
        answers = set(list(answers))
        groups.append(len(answers))
        answers = ""
# append the last answers to the list
answers = set(list(answers))
groups.append(len(answers))
print(sum(groups))
# Part One


# Part Two
groups = []
answers = list("abcdefghijklmnopqrstuvwxyz")
for line in puzzleInput:
    if line != "":
        # remove the answers that the people have not answerd "yes" to
        answers = [x for x in answers if x in list(line)]
    elif line == "":
        # save the amount of answers that the group answered "yes" to
        groups.append(len(answers))
        # reset the list to every possible answer
        answers = list("abcdefghijklmnopqrstuvwxyz")
groups.append(len(answers))
print(sum(groups))
# Part Two