# read input
with open('input.txt') as f:
    points = []
    folds = []
    grid_w, grid_h = 0, 0
    for s in f.readlines():
        s = s.rstrip()
        if not s: continue
        if ',' in s:
            x, y = int(s[:s.index(',')]), int(s[s.index(',')+1:])
            grid_w, grid_h = max(grid_w, x+1), max(grid_h, y+1)
            points.append((x, y))
        else:
            idx = s.index('=')
            folds.append({
                'type': s[idx-1 : idx],
                'size': int(s[idx+1:])
            })
    grid = [[' ' for i in range(grid_w)] for j in range(grid_h)]
    for pt in points:
        grid[pt[1]][pt[0]] = '#'

#----------part 1
# fold = folds[0]
# fold_size = fold['size']
# if fold['type'] == 'x':
#     for i in range(len(grid)):
#         a = grid[i][:fold_size].copy()
#         b = grid[i][fold_size+1:].copy()
#         for j in range(len(b)):
#             a[-1-j] = '#' if '#' in a[-1-j]+b[j] else '.'
#         grid[i] = a.copy()
# else:
#     b = grid[fold_size+1:]
#     grid = grid[:fold_size]
#     for i in range(len(b)):
#         grid[-1-i] = ['#' if '#' in pair else '.' for pair in zip(grid[-1-i], b[i])]

# ans = sum([x.count('#') for x in grid])
# print(ans)
#----------part 1


#----------part 2
for fold in folds:
    fold_size = fold['size']
    if fold['type'] == 'x':
        for i in range(len(grid)):
            a = grid[i][:fold_size].copy()
            b = grid[i][fold_size+1:].copy()
            for j in range(len(b)):
                a[-1-j] = '#' if '#' in a[-1-j]+b[j] else ' '
            grid[i] = a.copy()
    else:
        b = grid[fold_size+1:]
        grid = grid[:fold_size]
        for i in range(len(b)):
            grid[-1-i] = ['#' if '#' in pair else ' ' for pair in zip(grid[-1-i], b[i])]

for i in grid:
    print(''.join(i))
#----------part 2