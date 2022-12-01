import math
# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")


# Part One
busses = [int(x) for x in puzzleInput[1].split(",") if x != "x"]
earliestTime = int(puzzleInput[0])
lowestBusTime = 999999999999
lowestBus = 0

for e in busses:
    busTime = (earliestTime//e + 1)*e
    if busTime < lowestBusTime:
        lowestBusTime = busTime
        lowestBus = e
print("Part One answer : ", (lowestBusTime - earliestTime) * lowestBus)
# Part One

# Part Two - Chinese remainder theorem
# taken from geeks-website
def modInverse(a, m): 
    m0 = m 
    y = 0
    x = 1
    if (m == 1): 
        return 0

    while (a > 1): 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
    # Make x positive 
    if (x < 0): 
        x = x + m0 
  
    return x

delays = []
busses = [x for x in puzzleInput[1].split(",")]
for idx, item in enumerate(busses):
    if item != "x":
        delays.append(idx)
busses = [int(x) for x in puzzleInput[1].split(",") if x != "x"]

rem = [busses[x]-delays[x] for x in range(len(busses))]
product = math.prod(busses)
pp = [product//busses[x] for x in range(len(busses))]
inv = [modInverse(pp[x], busses[x]) for x in range(len(busses))]
mult = [pp[x]*rem[x]*inv[x] for x in range(len(busses))]
t = sum(mult) % product
print("Part Two answer : ", t)