# read input
with open('input.txt') as f:
    grid = [[int(x) for x in list(s.rstrip())] for s in f.readlines()]
    grid_w, grid_h = len(grid[0]), len(grid)


#----------part 1
# ans = 0
# for y in range(grid_h):
#     for x in range(grid_w):
#         current = grid[y][x]
#         if y > 0:  # check up
#             if grid[y-1][x] <= current:
#                 continue
#         if y < grid_h-1:  # check down
#             if grid[y+1][x] <= current:
#                 continue
#         if x > 0:  # check left
#             if grid[y][x-1] <= current:
#                 continue
#         if x < grid_w-1:  # check down
#             if grid[y][x+1] <= current:
#                 continue
#         ans += current + 1
# print(ans)
#----------part 1

#----------part 2
lows = []
for y in range(grid_h):
    for x in range(grid_w):
        current = grid[y][x]
        if y > 0:  # check up
            if grid[y-1][x] <= current:
                continue
        if y < grid_h-1:  # check down
            if grid[y+1][x] <= current:
                continue
        if x > 0:  # check left
            if grid[y][x-1] <= current:
                continue
        if x < grid_w-1:  # check down
            if grid[y][x+1] <= current:
                continue
        lows.append((x, y))

def flow(x, y, height):
    now = grid[y][x]
    if now in (9, '#'):
        return 0
    if now < height:
        return 0

    grid[y][x] = '#'
    count = 1
    if x > 0:
        count += flow(x-1, y, now)
    if x < grid_w-1:
        count += flow(x+1, y, now)
    if y > 0:
        count += flow(x, y-1, now)
    if y < grid_h-1:
        count += flow(x, y+1, now)
    return count

basins = []
for low in lows:
    basin = flow(low[0], low[1], 0)
    basins.append(basin)

a, b, c = sorted(basins)[-3:]
print(a*b*c)
#----------part 2