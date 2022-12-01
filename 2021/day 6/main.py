# read input
with open('input.txt') as f:
    indata = [int(x) for x in f.readline().rstrip().split(',')]
        
#----------part 1&2
fishes = [indata.count(i) for i in range(9)]
day_count = 256
for i in range(day_count):
    new_fishes = fishes[0]
    del fishes[0]  # left shift
    fishes[6] += new_fishes  # adult cycle
    fishes.append(new_fishes)  # new-borns
print(sum(fishes))
#----------part 1&2