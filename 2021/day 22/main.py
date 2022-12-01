# read input
with open('input.txt') as f:
    instructions = []
    min_r, max_r = 0, 0
    r = 0
    for s in f.readlines():
        s = s.strip()
        y_idx = s.index(',')+3
        z_idx = s.index(',', y_idx)+3
        data = [
            1 if s[:s.index(' ')] == 'on' else 0,  # bit
            int(s[s.index('=')+1:s.index('.')]),  # x1
            int(s[y_idx:s.index('.', y_idx)]),  # y1
            int(s[z_idx:s.index('.', z_idx)]),  # z1
            int(s[s.index('.')+2:s.index(',')]),  # x2
            int(s[s.index('.', y_idx)+2:s.index(',', y_idx)]),  # y2
            int(s[s.index('.', z_idx)+2:])  # z2
        ]
        instructions.append(data)
        min_r, max_r = min(min(data[1:]), min_r), max(max(data[1:]), max_r)
        r = max(abs(min_r), max_r)

#----------part 1
# import numpy as np
# r = 50
# grid = np.zeros((r*2+1, r*2+1, r*2+1), dtype=np.int8)
# for step in instructions:
#     bit = step[0]
#     x1, y1, z1, x2, y2, z2 = [x+r for x in step[1:]]

#     grid[x1:x2+1, y1:y2+1, z1:z2+1] = bit
# ans = np.count_nonzero(grid == 1)
# print(ans)
#----------part 1

#----------part 2
# i originaly used a dictionary as the grid, but then i saw a video where the guy
# used a 3D list as the grid. His sollution is about 10 times faster than mine
X, Y, Z = [], [], []
# divide grid
for idx, line in enumerate(instructions):
    print(f"Dividing line: {idx}", end ="\r", flush=True)
    x1, y1, z1, x2, y2, z2 = line[1:]
    x2 += 1
    y2 += 1
    z2 += 1
    # add the coordinates to the lists
    X = set(X)
    Y = set(Y)
    Z = set(Z)
    X.update([x1, x2])
    Y.update([y1, y2])
    Z.update([z1, z2])
    X = sorted(list(X))
    Y = sorted(list(Y))
    Z = sorted(list(Z))
# divide grid
print('\ndone dividing')

# color grid
w, h, l = len(X), len(Y), len(Z)
states = [ [ [ 0 for z in range(l) ] for y in range(h) ] for x in range(w)]
for idx, line in enumerate(instructions):
    print(f"Coloring line: {idx}", end ="\r", flush=True)
    bit = line[0]
    x1, y1, z1, x2, y2, z2 = line[1:]
    x2 += 1
    y2 += 1
    z2 += 1

    # update the states of the cuboids
    x_i1 = X.index(x1)
    x_i2 = X.index(x2, x_i1)
    y_i1 = Y.index(y1)
    y_i2 = Y.index(y2, y_i1)
    z_i1 = Z.index(z1)
    z_i2 = Z.index(z2, z_i1)

    for x in range(x_i1, x_i2):
        for y in range(y_i1, y_i2):
            for z in range(z_i1, z_i2):
                states[x][y][z] = bit
# color grid
print('\ndone coloring')

print('Calculating the result')
# count grid
ans = 0
for x in range(len(X)-1):
    for y in range(len(Y)-1):
        for z in range(len(Z)-1):
            bit = states[x][y][z]
            if bit == 1:
                x2, y2, z2 = X[x+1], Y[y+1], Z[z+1]
                ans += (x2-X[x])*(y2-Y[y])*(z2-Z[z])
# count grid

print(f'The answer is: {ans}')
#----------part 2