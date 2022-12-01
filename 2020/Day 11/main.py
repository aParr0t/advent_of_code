# read the input file
inputFile = open("input.txt", "r")
seats = inputFile.readlines()
for i in range(len(seats)):
    seats[i] = seats[i].rstrip("\n")

# This function is used for Part One
def adjacentNeighbours(i, j):
    neighbours = 0
    # count the neighbours around the given seat
    for y in range(j-1, j+2):
        for x in range(i-1, i+2):
            if x >= 0 and x < len(seats[0]) and y >= 0 and y < len(seats):
                if not(x == i and y == j):
                    if seats[y][x] == "#":
                        neighbours += 1
    return neighbours

def castRay(startX, startY, xVel, yVel):
    x, y = startX, startY
    while True:
        x += xVel
        y += yVel
        # Test if position is in bounds
        if x >= 0 and x < len(seats[0]) and y >= 0 and y < len(seats):
            # return the first seat the ray encounters
            if seats[y][x] == "#":
                return 1
            elif seats[y][x] == "L":
                return 0
        else:
            # return ympty seat if the ray reached the end
            return 0


# This function is used for Part Two
def visibleNeighbours(i, j):
    neighbours = 0
    # cast rays in every of the eight directions
    neighbours += castRay(i, j, -1, -1)
    neighbours += castRay(i, j, -1, 0)
    neighbours += castRay(i, j, -1, 1)
    neighbours += castRay(i, j, 0, -1)
    neighbours += castRay(i, j, 0, 1)
    neighbours += castRay(i, j, 1, -1)
    neighbours += castRay(i, j, 1, 0)
    neighbours += castRay(i, j, 1, 1)
    return neighbours


def applyRules(part):
    # rule nr. 2 depends on which part is selected
    if part == 1:
        rule2Threshold = 4
    elif part == 2:
        rule2Threshold = 5

    newSeats = []
    global seats
    for i in range(len(seats)):
        string = ""
        for j in range(len(seats[0])):
            # choose different methods of vounting neighbours depending on which part you are on
            if part == 1:
                neighbours = adjacentNeighbours(j, i)
            elif part == 2:
                neighbours = visibleNeighbours(j, i)

            # construct the new seats based on the rules
            if seats[i][j] == "L" and neighbours == 0:
                string += "#"
            elif seats[i][j] == "#" and neighbours >= rule2Threshold:
                string += "L"
            else:
                string += seats[i][j]
            
        newSeats.append(string)
    return newSeats

# Run the "simulation" until the seatMap does not change
roundCount = 0
newSeats = applyRules(2)
while seats != newSeats:
    seats = newSeats.copy()
    newSeats = applyRules(2)
    roundCount += 1
takenSeatCount = 0

# count the amount of seats that are occupied
for e in seats:
    takenSeatCount += e.count("#")
print("The answer for the chosen part: ", takenSeatCount)