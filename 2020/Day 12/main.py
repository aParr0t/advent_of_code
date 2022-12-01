# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# Part One
x, y = 0, 0
direction = 0
for line in puzzleInput:
    # read the command
    action = line[0]
    value = int(line[1:])

    # Move the ship in any of the 4 directions
    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    # Rotate the ship
    elif action == "L":
        direction = (direction - value + 360) % 360
    elif action == "R":
        direction = (direction + value) % 360
    # move the ship forwards in the pointing direction
    elif action == "F":
        if direction == 0:
            x += value
        elif direction == 90:
            y -= value
        elif direction == 180:
            x -= value
        elif direction == 270:
            y += value
print("Part One answer : ", abs(x) + abs(y))
# Part One

# Part Two
pointX, pointY = 10, 1
shipX, shipY = 0, 0
for line in puzzleInput:
    # read the command
    action = line[0]
    value = int(line[1:])

    # move the point in any of the 4 directions
    if action == "N":
        pointY += value
    elif action == "S":
        pointY -= value
    elif action == "E":
        pointX += value
    elif action == "W":
        pointX -= value
    # rotate the point around the ship
    elif action == "R":
        for i in range(value//90):
            temp = pointY
            pointY = -pointX
            pointX = temp
    elif action == "L":
        for i in range(value//90):
            temp = pointX
            pointX = -pointY
            pointY = temp
    # move the ship value number of times to the point
    elif action == "F":
        for e in range(value):
            shipX += pointX
            shipY += pointY
print("Part Two answer : ", abs(shipX) + abs(shipY))
# Part Two