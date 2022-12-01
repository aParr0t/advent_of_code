class Bag:
    def __init__(self):
        self.parents = []
        self.children = []
        self.childrenCounts = []
    
    def addParent(self, parentName):
        self.parents.append(parentName)
    
    def addChild(self, childName, childCount):
        self.children.append(childName)
        self.childrenCounts.append(childCount)

# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()

for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")


# Part One and Two
bagTree = {}
for line in puzzleInput:
    # get parent bag
    parentBag = line[:line.index("contain")-6]

    # split each line into the different bag info
    childrenBags = list(line[line.index("contain")+8:-1].split(", "))
    for counter, string in enumerate(childrenBags):
        # get the count and name of the bag
        if "no other" in string:
            childName = 0
            bagCount = 0
        else:
            bagCount = int(string[:1])
            childName = string[2:string.index("bag")-1]

        # add the bag info to the array
        childrenBags[counter] = [childName, bagCount]
    
    # add parent bag to dict
    if parentBag not in bagTree.keys():
        bagTree[parentBag] = Bag()

    # for every child of that parent, add the child to the dict
    for childBag in childrenBags:
        childBagName = childBag[0]
        count = childBag[1]
        if childBagName not in bagTree.keys():
            bagTree[childBagName] = Bag()
        bagTree[childBagName].addParent(parentBag)
        bagTree[parentBag].addChild(childBagName, count)

# count the unique colors that the bag could be held in
colors = []
def findColorsOfBag(bagName):
    # base case
    if len(bagTree[bagName].parents) == 0:
        colors.append(bagName)
    # recursive case
    else:
        colors.append(bagName)
        for e in bagTree[bagName].parents:
            findColorsOfBag(e)
findColorsOfBag("shiny gold")
colors = list(set(colors))
colors.remove("shiny gold")
print("Part One answer: " + str(len(colors)))


# Count the number of individual bags inside a bag
bagCount = []
def countBagsInsideBag(bagName, multiplier):
    if len(bagTree[bagName].children) == 0:
         pass
    else:
        for index, child in enumerate(bagTree[bagName].children):
            count = int(bagTree[bagName].childrenCounts[index])
            bagCount.append(count*multiplier)
            countBagsInsideBag(child, count*multiplier)
countBagsInsideBag("shiny gold", 1)
print("Part Two answer : " + str(sum(bagCount)))
# Part One and Two
