import functools
import heapq
from collections import Counter, defaultdict, deque
from copy import deepcopy

# read input
L = [s.rstrip() for s in open("input.txt")]
G = [[c for c in s] for s in L]
w, h = len(L[0]), len(L)


class Module:
    def __init__(self, name: str, con: list[str]):
        self.name = name
        self.con = con

    def recieve_pulse(self, pulse: int, origin):
        for c in self.con:
            P.append((c, pulse, self.name))


class FlipFlop(Module):
    def __init__(self, name, con):
        super().__init__(name, con)
        self.on = False

    def recieve_pulse(self, pulse, origin):
        if pulse == 1:
            return
        send = 1 if not self.on else 0
        self.on = not self.on
        for c in self.con:
            P.append((c, send, self.name))


class Conjunction(Module):
    def __init__(self, name, con):
        super().__init__(name, con)
        self.mem = {}

    def recieve_pulse(self, pulse, module):
        global i, cycles
        self.mem[module] = pulse
        if all([p == 1 for p in self.mem.values()]):
            if self.name in ["ls", "dc", "qm", "jh", "zq"]:
                if self.name not in cycles:
                    cycles[self.name] = i
            send = 0
        else:
            send = 1
        for c in self.con:
            P.append((c, send, self.name))


class Broadcast(Module):
    def __init__(self, name, con):
        super().__init__(name, con)


# setup modules
M: dict[str, Module] = defaultdict(lambda: Module("output", []))
for l in L:
    a, b = l.split(" -> ")
    con = b.split(", ")
    name = a[1:]
    if a.startswith("%"):
        m = FlipFlop(name, con)
    elif a.startswith("&"):
        m = Conjunction(name, con)
    else:
        m = Broadcast(a, con)
        name = a
    M[name] = m

# initialize conjunction inputs
for name, m in list(M.items()):
    for c in m.con:
        dest = M[c]
        if isinstance(dest, Conjunction):
            dest.mem[name] = 0

# ----------part 1
# Part 1 was straight forward
_M = deepcopy(M)

count = [0, 0]
for i in range(1000):
    P = [["broadcaster", 0, "button"]]
    while P:
        name, p, origin = P.pop(0)
        intensity = "low" if p == 0 else "high"
        count[p] += 1
        m = _M[name]
        m.recieve_pulse(p, origin)


res = count[0] * count[1]

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
# Saw that each junction sends out a low pulse in cycles of the same size
# every time. I have hardcoded the specific junctions into the code. I picked
# them from the input because they were responsible for sending the low signals
# to the "ls" module, which then would send a signal to the "rx" module.
# The solution is "simply" the product of the cycle lengths.
_M = deepcopy(M)

res = 0
found = False

cycles = {}
i = 0
while not found:
    P = [("broadcaster", 0, "button")]
    i += 1
    while P:
        name, p, origin = P.pop(0)
        intensity = "low" if p == 0 else "high"
        m = _M[name]
        m.recieve_pulse(p, origin)
    if len(cycles) == 4:
        break

res = 1
for c in cycles.values():
    res *= c

print(f"Part 2 answer: {res}")
# ----------part 2
