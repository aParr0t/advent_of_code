inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()

for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# variable initialization
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


# this bit of code is used by both parts of the puzzle
# read and parse data from puzzleInput and save it as different passports
passports = []
passport = {}
for line in puzzleInput:
    if line != "":
        # split the string into the different fields and then split those fields by key and value
        data = line.split(" ")
        for info in data:
            field = info.split(":")
            passport[field[0]] = field[1]
    elif line == "":
        # save the current passport into the passports array if a new passport is coming
        passports.append(passport)
        passport = {}
passports.append(passport)


# Part One
validCounter = 0
for counter, passport in enumerate(passports):
    # checking the fields that the passport has
    missing = requiredFields.copy()
    for key in passport.keys():
        if key in requiredFields:
            missing.remove(key)

    # checking if the passport has all of the required fields
    if len(missing) > 1:
        continue
    if len(missing) == 1 and missing[0] != "cid":
        continue
    validCounter += 1
print(validCounter)
# Part One


# Part Two
validCounter = 0
for counter, passport in enumerate(passports):
    # checking the fields that the passport has
    missing = requiredFields.copy()
    for key in passport.keys():
        if key in requiredFields:
            missing.remove(key)

    # checking if the passport has all of the required fields
    if len(missing) > 1:
        continue
    if len(missing) == 1 and missing[0] != "cid":
        continue

    # check if every field is valid
    # check birth year
    value = int(passport["byr"])
    if value < 1920 or value > 2002:
        continue

    # check issue year
    value = int(passport["iyr"])
    if value < 2010 or value > 2020:
        continue

    # check expiration year
    value = int(passport["eyr"])
    if value < 2020 or value > 2030:
        continue

    # check height
    value = passport["hgt"]
    unitOfMeasure = value[len(value) - 2] + value[len(value) - 1]
    try:
        num = int(value[: len(value) - 2])
    except ValueError:
        continue
    if unitOfMeasure == "cm":
        if num < 150 or num > 193:
            continue
    elif unitOfMeasure == "in":
        if num < 59 or num > 76:
            continue
    else:
        # passport is invalid if there is no unit of measure
        continue

    # check hair color:
    value = passport["hcl"]
    if value[0] != "#":
        continue
    color = value[1:]
    # check if color has only characters a-f and numbers 0-9
    try:
        int(color, 16)
    except ValueError:
        continue

    # check eye color
    value = passport["ecl"]
    if value not in eyeColors:
        continue

    # check Passport ID
    value = passport["pid"]
    if len(value) != 9:
        continue

    validCounter += 1
print(validCounter)
# Part Two
