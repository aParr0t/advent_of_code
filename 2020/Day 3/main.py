inputFile = open("input.txt", "r")
inputStrings = inputFile.readlines()

for i in range(len(inputStrings)):
    inputStrings[i] = inputStrings[i].rstrip("\n")


# Part One
slopes = [[3, 1]]
# Part One

# Part Two
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
# Part Two

# the code below works for both parts
productOfTrees = 1
for slope in slopes:
    x, y, counter = 0, 0, 0
    for i in range(len(inputStrings)):
        # go down the slope
        x = (x+slope[0])%len(inputStrings[0])
        y = (y+slope[1])

        # exit loop if reached the bottom of list
        if y >= len(inputStrings):
            break
        
        # change tree counter by 1 if hit a tree
        line = inputStrings[y]
        if line[x] == "#":
            counter += 1
            
    # multiply the number of times you hit a tree
    productOfTrees *= counter
print(productOfTrees)