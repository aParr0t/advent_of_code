# read input
with open('input.txt') as f:
    indata = list(map(
        lambda x: x.rstrip(),
        f.readlines()
        ))

#----------part 1
# pos = [0, 0]
# for s in indata:
#     action = s[:s.index(' ')]
#     step = int(s[s.index(' ')+1:])
#     if action == 'forward':
#         pos[0] += step
#     elif action == 'down':
#         pos[1] += step
#     if action == 'up':
#         pos[1] -= step

# print(pos[0]*pos[1])
#----------part 1


#----------part 2
pos = [0, 0]
aim = 0
for s in indata:
    action = s[:s.index(' ')]
    step = int(s[s.index(' ')+1:])
    if action == 'forward':
        pos[0] += step
        pos[1] += aim * step
    elif action == 'down':
        aim += step
    if action == 'up':
        aim -= step

print(pos[0]*pos[1])
#----------part 2