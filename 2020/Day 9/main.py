# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i].rstrip("\n"))

# Part One and Two
preambleSize = 25
def validNumber(num, preamble):
    for i in range(len(preamble)):
        # if the remainder of next number minus the number in preamble is in the preamble then the next number is valid
        if (num-preamble[i]) in preamble and preamble.index(num-preamble[i]) != i:
            return True
    return False

# find the number that is not valid
for i in range(preambleSize, len(puzzleInput)):
    if not validNumber(puzzleInput[i], puzzleInput[i-preambleSize:i]):
        invalidNum = puzzleInput[i]
print("Part One answer : ", invalidNum)

# brute force the sollution with two pointer, i and j. 
for i in range(len(puzzleInput)-2):
    for j in range(i+2, len(puzzleInput)):
        # if the sum of the contiguous set is the invalidNumber then it means that we have found the correct set
        addedNums = sum(puzzleInput[i:j])
        if addedNums == invalidNum:
            contiguousSet = puzzleInput[i:j]
            print("Part Two answer : ", max(contiguousSet)+min(contiguousSet))
        # if the sum 
        elif addedNums > invalidNum:
            break
# Part One and Two