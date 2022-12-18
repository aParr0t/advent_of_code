import sys

sys.setrecursionlimit(99999)

# read input
cubes = [s.rstrip("\n").split(",") for s in open("input.txt")]
cubes = [tuple([int(x) for x in pos]) for pos in cubes]


# ----------both parts
w = 30
grid = [[[0 for z in range(w)] for y in range(w)] for x in range(w)]
for (x, y, z) in cubes:
    grid[x][y][z] = 1

adj = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

# ----------both parts

# ----------part 1
def faces(x, y, z):
    visited.add((x, y, z))
    face_count = 6
    for (dx, dy, dz) in adj:
        nx, ny, nz = x + dx, y + dy, z + dz
        # rewrite as? not (0 <= nx < w and 0 <= ny < w and 0 <= nz < w)
        if nx < 0 or nx >= w or ny < 0 or ny >= w or nz < 0 or nz >= w:
            continue
        if grid[nx][ny][nz] == 0:
            continue
        face_count -= 1
        if (nx, ny, nz) not in visited:
            face_count += faces(nx, ny, nz)
    return face_count


visited = set()
face_sum = 0
for cube in cubes:
    if cube not in visited:
        face_sum += faces(*cube)

print(f"Part 1 answer: {face_sum}")
# ----------part 1

# ----------part 2
def scan_water(x, y, z):
    water.add((x, y, z))
    for (dx, dy, dz) in adj:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < 0 or nx >= w or ny < 0 or ny >= w or nz < 0 or nz >= w:
            continue
        if grid[nx][ny][nz] == 1:
            continue
        if (nx, ny, nz) not in water:
            scan_water(nx, ny, nz)


def faces(x, y, z):
    visited.add((x, y, z))
    face_count = 6
    for (dx, dy, dz) in adj:
        nx, ny, nz = x + dx, y + dy, z + dz
        if nx < 0 or nx >= w or ny < 0 or ny >= w or nz < 0 or nz >= w:
            continue
        if grid[nx][ny][nz] == 0:
            if (nx, ny, nz) not in water:
                face_count -= 1
            continue
        face_count -= 1
        if (nx, ny, nz) not in visited:
            face_count += faces(nx, ny, nz)
    return face_count


water = set()
scan_water(0, 0, 0)

visited = set()
face_sum = 0
for cube in cubes:
    if cube not in visited:
        face_sum += faces(*cube)

print(f"Part 2 answer: {face_sum}")
# ----------part 2
