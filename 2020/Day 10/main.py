# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i].rstrip("\n"))

# Part One
puzzleInput.sort()
counts = {1 : 1, 2 : 0, 3 : 1}
for i in range(len(puzzleInput)-1):
    counts[puzzleInput[i+1]-puzzleInput[i]] += 1

print("Part One answer : ", str(counts[1]*counts[3]))
# Part One


# Part Two
tree = {}
def createTree(num):
    # get all numbers that are less than or equal to 3 spaces away from current num
    arrangements = [x for x in puzzleInput if x > num and x <= num+3]
    if len(arrangements) == 0:
        return
    if num not in tree.keys():
        tree[num] = []
        tree[num] = tree[num] + arrangements
        for e in arrangements:
            createTree(e)

def cleanTree():
    for e in tree.keys():
        # remove any duplicate pointer/values
        tree[e] = list(set(tree[e]))

highestNum = max(puzzleInput)
memoize = {}
def countArrangements(num):
    if num == highestNum:
        return 1
    if num in memoize:
        return memoize[num]
    memoize[num] = sum([countArrangements(x) for x in tree[num]])
    return memoize[num]

createTree(0)
cleanTree()
print("Part Two answer : ", countArrangements(0))
# Part Two