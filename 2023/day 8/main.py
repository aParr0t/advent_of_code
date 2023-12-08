import math

# read input
inp = [s.rstrip() for s in open("input.txt")]

D = inp[0].replace("L", "0").replace("R", "1")
D = [int(x) for x in D]
d_len = len(D)

N = {}
for l in inp[2:]:
    s = l[: l.index("=") - 1]
    left = l[l.index("(") + 1 : l.index(",")]
    right = l[l.index(",") + 2 : -1]
    N[s] = [left, right]

# ----------part 1
c = "AAA"
cnt = 0
d_idx = 0
while c != "ZZZ":
    c = N[c][D[d_idx]]
    d_idx = (d_idx + 1) % d_len
    cnt += 1

print(f"Part 1 answer: {cnt}")
# ----------part 1


# ----------part 2
C = [k for k in N.keys() if k.endswith("A")]  # starting nodes
# storing number of steps between encounters of nodes that end with Z
Z = [[] for _ in C]
CT = [0 for _ in C]  # the counters for each traveling node

d_idx = 0
while True:
    # increment all counters by 1
    for i in range(len(CT)):
        CT[i] += 1

    # take one step with each node
    for i, c in enumerate(C):
        C[i] = N[c][D[d_idx]]
        # save encounter of a node with Z
        if C[i].endswith("Z"):
            Z[i].append(CT[i])
            CT[i] = 0

    # exit when all nodes have found a loop
    if all([len(z) > 1 for z in Z]):
        break
    d_idx = (d_idx + 1) % d_len

# result will be the first time all nodes end up on a "Z"-node simultaneously
# this will be the lowest common multiple of the lengths of the loops
res = math.lcm(*[z[0] for z in Z])

print(f"Part 2 answer: {res}")
# ----------part 2
