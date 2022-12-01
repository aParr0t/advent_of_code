from search import astar
# read input
with open('input.txt') as f:
    grid = [[int(x) for x in list(s.rstrip())] for s in f.readlines()]
    gw, gh = len(grid[0]), len(grid)

#----------part 1
# path = astar(grid, [0, 0], [gw-1, gh-1])
# risk = sum([ grid[x[1]][x[0]] for x in path ])
# print('Risk level:', risk)
#----------part 1

#----------part 2 takes about 20sec
# tile the grid
old_gw, old_gh = len(grid[0]), len(grid)
grid = [row*5 for row in grid]
height = len(grid)
for i in range(4):
    for y in range(height):
        grid.append(grid[y].copy())

# increment grid
gw, gh = len(grid[0]), len(grid)
for y in range(gh):
    for x in range(gw):
        tile = (grid[y][x] + (y//old_gw) + (x//old_gh))
        if tile > 9:
            tile -= 9
        grid[y][x] = tile

gw, gh = len(grid[0]), len(grid)
path = astar(grid, [0, 0], [gw-1, gh-1])
risk = sum([ grid[x[1]][x[0]] for x in path ])
print('Risk level:', risk)
#----------part 2