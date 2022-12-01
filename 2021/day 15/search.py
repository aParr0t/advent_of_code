def astar(grid: list, start: list, end: list):
    grid_w, grid_h = len(grid[0]), len(grid)
    INFINITY = 999999
    def dist(n1: list, n2: list):
        return grid[n1[1]][n1[0]]

    def reconstruct_path(c):
        total_path = [c]
        while True:
            c = camefrom[c[1]][c[0]]
            if c == start:
                break
            total_path.append(c)
        
        return total_path
    
    def h(node: list):
        x1, y1 = node
        x2, y2 = end
        return abs(x2-x1) + abs(y2-y1)

    def neighbors(node: list):
        neighbor_list = []
        nx, ny = node
        for x in range(nx-1, nx+2):
            for y in range(ny-1, ny+2):
                # avoid checking yourself
                if x == nx and y == ny: continue
                # avoid diagonals
                if x != nx and y != ny: continue
                # avoid out of range
                if x < 0 or x > grid_w-1 or y < 0 or y > grid_h-1: continue

                neighbor_list.append([x, y])
        return neighbor_list

    openset = [start]
    camefrom = [[0 for x in range(grid_w)] for y in range(grid_h)]

    gscore = [[INFINITY for x in range(grid_w)] for y in range(grid_h)]
    gscore[start[1]][start[0]] = 0

    fscore = [[INFINITY for x in range(grid_w)] for y in range(grid_h)]
    fscore[start[1]][start[0]] = h(start)

    while len(openset) > 0:
        openset = sorted(openset, key=lambda x: fscore[x[1]][x[0]], reverse=True)
        current = openset.pop()
        
        if current == end:
            return reconstruct_path(end)

        adjacent = neighbors(current)
        for adj in adjacent:
            tentative_gScore = gscore[current[1]][current[0]] + dist(current, adj)
            if tentative_gScore < gscore[adj[1]][adj[0]]:
                camefrom[adj[1]][adj[0]] = current
                gscore[adj[1]][adj[0]] = tentative_gScore
                fscore[adj[1]][adj[0]] = tentative_gScore + h(adj)
                if adj not in openset:
                    openset.append(adj)
    
    print("[FAILURE] Open set is empty but goal was never reached")

    