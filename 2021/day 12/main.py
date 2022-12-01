# read input
with open('input.txt') as f:
    graph = {}
    for s in f.readlines():
        s = s.strip()
        a = s[:s.index('-')]
        b = s[s.index('-')+1:]
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

#----------part 1
# ans = 0
# def search(node, small_caves):
#     if node == 'end':
#         global ans
#         ans += 1
#         return
#     if node.islower():
#         small_caves.append(node)  # mark visited
#     ways = [x for x in graph[node] if x not in small_caves]  # ignore visited
#     for way in ways:
#         search(way, small_caves.copy())  # recursive breadt-first search

# search('start', [])
# print(ans)
#----------part 1

#----------part 2
paths = []
def search(node, path, small_caves, double=None):
    path += node + ','
    if node == 'end':
        global paths
        paths.append(path)
        return
    
    if node.islower():
        small_caves.append(node)

    ways = []
    for x in graph[node]:
        if x == 'start':
            continue
        if x in small_caves and x != double:
            continue
        ways.append(x)
    
    for way in ways:
        if way == double:
            search(way, path, small_caves.copy(), '#')
        else:
            search(way, path, small_caves.copy(), double)
        
        if way.islower() and double==None:
            search(way, path, small_caves.copy(), way)

search('start', '', [])
print(len(set(paths)))
#----------part 2