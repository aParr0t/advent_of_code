# read input
with open('input.txt') as f:
    lines = [s.rstrip() for s in f.readlines()]
    grid = ''.join(lines)
    gw, gh = len(lines[0]), len(lines)
    
#----------part 1
steps = 0
prev_grid = ''
while prev_grid != grid:
    steps += 1
    prev_grid = grid
    # move horizontally
    new_grid = ''
    for y in range(0, len(grid), gw):
        row = grid[y:y+gw]
        wrap = False
        if row[0] == '.' and row[-1] == '>':
            wrap = True
        row = row.replace('>.', '.>')
        if wrap:
            row = '>' + row[1:-1] + '.'
        new_grid += row
    grid = new_grid

    # move vertically
    cols = []
    for x in range(gw):
        col = ''.join([grid[i] for i in range(x, len(grid), gw)])
        wrap = False
        if col[0] == '.' and col[-1] == 'v':
            wrap = True
        col = col.replace('v.', '.v')
        if wrap:
            col = 'v' + col[1:-1] + '.'
        cols.append(col)
    
    # merge the columns
    grid = ''
    for y in range(gh):
        for x in range(gw):
            grid += cols[x][y]

print(steps)
#----------part 1

#----------part 2

#----------part 2