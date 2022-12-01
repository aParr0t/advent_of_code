# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# Part One
mem = {}
mask = ""
for line in puzzleInput:
    if "ma" in line:
        # set the mask
        mask = list(line[7:])
    else:   
        # convert the int to binary and split the binary num into a list
        num = list('{0:036b}'.format(int(line[line.index("=")+2:])))
        # set the mask on the binary number list
        for i in range(len(mask)):
            if mask[i] != "X":
                num[i] = mask[i]
        # convert the binary num list back to a num and save it to memory
        mem[line[4:line.index("]")]] = int("".join(num), 2)

print("Part One answer : ", sum(mem.values()))
# Part One


# Part Two
mem = {}
mask = ""
for line in puzzleInput:
    if "ma" in line:
        # set the mask
        mask = list(line[7:])
    else:   
        # convert the int to binary and split the binary num into a list
        adress = list('{0:036b}'.format(int(line[4:line.index("]")])))

        # set the mask on the binary adress list
        pos = []
        for i in range(len(mask)):
            if mask[i] == "1":
                adress[i] = "1"
            elif mask[i] == "X":
                pos.append(i)
        
        # calculate the number of different arrangements
        posLen = len(pos)
        floats = 2**posLen

        # save the value in every possible adress
        for e in range(0, floats):
            # make a list of the arrangement
            arrangement = list(format(e, "0"+str(posLen)+"b"))

            # change the adress into the new arrangement
            for x in range(posLen):
                adress[pos[x]] = arrangement[x]
            
            # save the value in the new adress
            newAdress = int("".join(adress), 2)
            mem[newAdress] = int(line[line.index("=")+2:])
print("Part Two answer : ", sum(mem.values()))
# Part Two