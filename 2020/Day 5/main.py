inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()

for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# Part One
highestSeatID = 0
for string in puzzleInput:
    # find the seat row
    row = string[:7]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)

    # findt the seat column
    column = string[7:]
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)

    seatID = row*8+column
    highestSeatID = max(highestSeatID, seatID)
print(highestSeatID)
# Part One


# Part Two
passes = []
emptySeats = [x for x in range(0, int("1111111", 2)*8+int("111", 2)+1)]
for string in puzzleInput:
    # find the seat row
    row = string[:7]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)

    # findt the seat column
    column = string[7:]
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)

    seatID = row*8+column
    if seatID in emptySeats:
        emptySeats.remove(seatID)

# find the correct seat
for i in range(len(emptySeats)-1):
    if emptySeats[i+1] - emptySeats[i] != 1:
        print(emptySeats[i+1])
        break
# Part Two