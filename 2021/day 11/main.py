# read input
with open('input.txt') as f:
    grid = [[int(x) for x in s.rstrip()] for s in f.readlines()]
    grid_w, grid_h = len(grid[0]), len(grid)

#----------part 1
# ans = 0

# def flash(x, y):
#     global ans
#     ans += 1
#     grid[y][x] = '#'
#     for i in range(y-1, y+2):
#         for j in range(x-1, x+2):
#             if (0 <= j < grid_w) and (0 <= i < grid_h):
#                 if grid[i][j] == '#':
#                     continue

#                 grid[i][j] += 1
#                 if grid[i][j] > 9:
#                     flash(j, i)

# for step in range(100):
#     for i in range(grid_h):
#         grid[i] = [x+1 for x in grid[i]]

#     for i in range(grid_h):
#         for j in range(grid_w):
#             if grid[i][j] == '#':
#                 continue
                
#             if grid[i][j] > 9:
#                 flash(j, i)

#     for i in range(len(grid)):
#         grid[i] = [0 if x=='#' else x for x in grid[i]]
# print(ans)
#----------part 1


#----------part 2
count = 0

def flash(x, y):
    global count
    count += 1
    grid[y][x] = '#'
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (0 <= j < grid_w) and (0 <= i < grid_h):
                if grid[i][j] == '#':
                    continue

                grid[i][j] += 1
                if grid[i][j] > 9:
                    flash(j, i)
step = 0
while True:
    step += 1
    count = 0
    for i in range(grid_h):
        grid[i] = [x+1 for x in grid[i]]

    for i in range(grid_h):
        for j in range(grid_w):
            if grid[i][j] == '#':
                continue
                
            if grid[i][j] > 9:
                flash(j, i)

    for i in range(len(grid)):
        grid[i] = [0 if x=='#' else x for x in grid[i]]
    
    if count == grid_h*grid_w:
        print(step)
        break
#----------part 2