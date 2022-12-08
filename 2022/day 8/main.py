# read input
trees = [[int(x) for x in s.rstrip("\n")] for s in open("input.txt")]

# ----------both parts
grid_w, grid_h = len(trees[0]), len(trees)
visible = [[0 for x in range(grid_w)] for y in range(grid_h)]

# scan vertically
for [start, end, step] in [[0, grid_h, 1], [grid_h - 1, -1, -1]]:
    for x in range(0, grid_w):
        highest = -1
        for y in range(start, end, step):
            tree = trees[y][x]
            if tree > highest:
                highest = tree
                visible[y][x] = 1

# scan horizontally
for [start, end, step] in [[0, grid_w, 1], [grid_w - 1, -1, -1]]:
    for y in range(0, grid_w):
        highest = -1
        for x in range(start, end, step):
            tree = trees[y][x]
            if tree > highest:
                highest = tree
                visible[y][x] = 1
# ----------both parts

# ----------part 1
visible_count = sum([sum(row) for row in visible])
print(f"Part 1 answer: {visible_count}")
# ----------part 1

# ----------part 2
def scenic_score(tree_x, tree_y):
    this_tree = trees[tree_y][tree_x]
    score = 1

    # scan vertically
    for [start, end, step] in [[tree_y + 1, grid_h, 1], [tree_y - 1, -1, -1]]:
        distance = 0
        for y in range(start, end, step):
            distance += 1
            tree = trees[y][tree_x]
            if tree >= this_tree:
                break
        score *= distance

    # scan horizontally
    for [start, end, step] in [[tree_x + 1, grid_w, 1], [tree_x - 1, -1, -1]]:
        distance = 0
        for x in range(start, end, step):
            distance += 1
            tree = trees[tree_y][x]
            if tree >= this_tree:
                break
        score *= distance

    return score


highest_score = 0
for y in range(1, grid_h - 1):
    for x in range(1, grid_w - 1):
        if visible[y][x] == 1:
            highest_score = max(highest_score, scenic_score(x, y))

print(f"Part 2 answer: {highest_score}")
# ----------part 2
