# read input
map = [list(s.rstrip("\n")) for s in open("input.txt")]


# ----------both parts
map_w, map_h = len(map[0]), len(map)
for y, row in enumerate(map):
    for x, height_code in enumerate(row):
        if height_code == "S":
            start = (x, y)
            map[y][x] = ord("a")
        elif height_code == "E":
            end = (x, y)
            map[y][x] = ord("z")
        else:
            map[y][x] = ord(height_code)


# ----------both parts

# ----------part 1
visited = [[99999 for x in range(map_w)] for y in range(map_h)]


def search(x, y):
    visited[y][x] = 0
    to_visit = []
    to_visit.append((x, y))

    while len(to_visit) > 0:
        vx, vy = to_visit.pop()
        current_height = map[vy][vx]
        current_steps = visited[vy][vx]

        neighbor_directions = [
            (0, -1),  # up
            (0, 1),  # down
            (1, 0),  # right
            (-1, 0),  # left
        ]
        for direction in neighbor_directions:
            nx, ny = vx + direction[0], vy + direction[1]
            if nx < 0 or nx >= map_w or ny < 0 or ny >= map_h:
                continue

            neighbor_height = map[ny][nx]
            isNeighborClimbable = neighbor_height <= current_height + 1
            isNeighborCloser = current_steps + 1 < visited[ny][nx]

            if isNeighborClimbable and isNeighborCloser:
                if (nx, ny) == end:
                    return current_steps + 1

                # insert at correct position
                for i, pos in enumerate(to_visit):
                    if visited[pos[1]][pos[0]] < current_steps + 1:
                        to_visit.insert(i, (nx, ny))
                        break
                else:
                    to_visit.append((nx, ny))

                visited[ny][nx] = current_steps + 1


fewest_steps = search(start[0], start[1])

print(f"Part 1 answer: {fewest_steps}")
# ----------part 1

# ----------part 2
visited = [[99999 for x in range(map_w)] for y in range(map_h)]


def reverse_search(x, y):
    visited[y][x] = 0
    to_visit = []
    to_visit.append((x, y))

    while len(to_visit) > 0:
        vx, vy = to_visit.pop()
        current_height = map[vy][vx]
        current_steps = visited[vy][vx]

        neighbor_directions = [
            (0, -1),  # up
            (0, 1),  # down
            (1, 0),  # right
            (-1, 0),  # left
        ]
        for direction in neighbor_directions:
            nx, ny = vx + direction[0], vy + direction[1]
            if nx < 0 or nx >= map_w or ny < 0 or ny >= map_h:
                continue

            neighbor_height = map[ny][nx]
            isNeighborClimbable = current_height - 1 <= neighbor_height
            isNeighborCloser = current_steps + 1 < visited[ny][nx]

            if isNeighborClimbable and isNeighborCloser:
                if neighbor_height == ord("a"):
                    return current_steps + 1

                # insert at correct position
                for i, pos in enumerate(to_visit):
                    if visited[pos[1]][pos[0]] < current_steps + 1:
                        to_visit.insert(i, (nx, ny))
                        break
                else:
                    to_visit.append((nx, ny))

                visited[ny][nx] = current_steps + 1


fewest_steps = reverse_search(end[0], end[1])

print(f"Part 2 answer: {fewest_steps}")
# ----------part 2
