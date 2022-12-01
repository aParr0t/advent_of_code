# read input
with open("input.txt") as f:
    positions = [int(x) for x in f.readline().rstrip().split(',')]

#----------part 1
# positions = sorted(positions)
# goal_pos = positions[len(positions)//2]  # median

# fuel_count = sum([abs(goal_pos-x) for x in positions])  # sum of the linear distances
# print(fuel_count)
#----------part 1

#----------part 2
import math
goal_pos_1 = math.floor(sum(positions) / len(positions))  # lower mean
goal_pos_2 = math.ceil(sum(positions) / len(positions))  # higher mean

diff = [abs(goal_pos_1-x) for x in positions]  # linear distance
fuel_count_1 = sum([sum(range(1, x+1)) for x in diff])  # lower mean

diff = [abs(goal_pos_2-x) for x in positions]  # linear distance
fuel_count_2 = sum([sum(range(1, x+1)) for x in diff])  # higher mean
print(min(fuel_count_1, fuel_count_2))  # pick the one that's lowest
#----------part 2