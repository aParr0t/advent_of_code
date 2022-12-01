inputFile = open("input.txt", "r")
strings = inputFile.readlines()

for i in range(len(strings)):
    strings[i] = strings[i].rstrip("\n")

# Part One
counter = 0
for line in strings:
    minOccurence = int(line[0:line.index("-")])
    maxOccurence = int(line[line.index("-")+1:line.index(" ")])
    policyLetter = line[line.index(":")-1:line.index(":")]
    password = line[line.index(":")+2:]
    occurence = password.count(policyLetter)
    if occurence >= minOccurence and occurence <= maxOccurence:
        counter += 1
print(counter)
# Part One

# Part Two
counter = 0
for line in strings:
    index1 = int(line[0:line.index("-")])-1
    index2 = int(line[line.index("-")+1:line.index(" ")])-1
    policyLetter = line[line.index(":")-1:line.index(":")]
    password = line[line.index(":")+2:]
    letterCheck = 0
    if (password[index1] == policyLetter):
        letterCheck += 1
    if (password[index2] == policyLetter):
        letterCheck += 1
    if (letterCheck == 1):
        counter += 1
print(counter)
# Part Two