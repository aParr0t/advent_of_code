# read input
with open('input.txt') as f:
    s = f.readline().rstrip()
    x1 = int(s[s.index('=')+1:s.index('.')])
    x2 = int(s[s.index('.')+2:s.index(',')])
    i = s.index('y=')
    y1 = int(s[i+2:s.index('.', i)])
    y2 = int(s[s.index('.', i)+2:])

#----------part 1
# max_vel = abs(y1+1)
# ans = sum([x for x in range(1, max_vel+1)])
# print(ans)
#----------part 1

#----------part 2 dogshit code
max_vel = abs(y1+1)
valid_steps = {x: [] for x in range(1, max_vel*3)}  # arbitrary 100
for y in range(y1, max_vel+1):
    steps = 0
    pos = 0
    vel = y
    while True:
        pos += vel
        steps += 1
        vel -= 1
        if y1 <= pos <= y2:
            valid_steps[steps].append(y)
        elif pos < y1-1:
            break

ans = 0
for x in range(1, x2+1):
    steps = 0
    pos = 0
    vel = x
    checked = []
    delay = 0
    while True:
        pos += vel
        steps += 1
        if vel > 0:
            vel -= 1

        if pos > x2:
            break

        if x1 <= pos <= x2:
            if steps in valid_steps:
                new = [x for x in valid_steps[steps] if x not in checked]
            ans += len(new)
            checked.extend(new)
        if vel == 0:
            delay += 1
            if delay > max_vel*3:
                break
print(ans)
#----------part 2