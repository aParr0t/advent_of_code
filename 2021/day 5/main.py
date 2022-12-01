# read input
with open('input.txt') as f:
    lines = [x.rstrip() for x in f.readlines()]
    for i in range(len(lines)):
        s = lines[i]
        lines[i] = [
            int(s[:s.index(',')]),
            int(s[s.index(',')+1 : s.index('-')-1]),
            int(s[s.index('>')+2 : s.index(',', s.index('-'))]),
            int(s[s.index(',', s.index('-'))+1:])
        ]
    max_width = max([max(x[0], x[2]) for x in lines])+1
    max_height = max([max(x[1], x[3]) for x in lines])+1
grid = [[0 for i in range(max_width)] for j in range(max_height)]

#----------part 1
# for line in lines:
#     x1, x2 = min(line[0], line[2]), max(line[0], line[2])
#     y1, y2 = min(line[1], line[3]), max(line[1], line[3])
#     if x2-x1 != 0 and y2-y1 != 0: # diagonals
#         continue
    
#     for x in range(x1, x2+1):
#         for y in range(y1, y2+1):
#             grid[y][x] += 1
    
# ans = sum([sum([1 for x in row if x >= 2]) for row in grid])
# print(ans)
#----------part 1


#----------part 2
for line in lines:
    x1, y1, x2, y2 = line
    if abs(x2-x1) != 0 and abs(y2-y1) != 0: # diagonals
        x_step = -1 if x2 < x1 else 1
        y_step = -1 if y2 < y1 else 1
        x_vals = list(range(x1, x2, x_step))
        x_vals.append(x2)
        y_vals = list(range(y1, y2, y_step))
        y_vals.append(y2)
        points = zip(x_vals, y_vals)
    
        for point in points:
            grid[point[1]][point[0]] += 1
    else: # straight lines
        x1, x2 = min(line[0], line[2]), max(line[0], line[2])
        y1, y2 = min(line[1], line[3]), max(line[1], line[3])
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[y][x] += 1

ans = sum([sum([1 for x in row if x >= 2]) for row in grid])
print(ans)
#----------part 2