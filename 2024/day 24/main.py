# ----------common for both parts
import sys
import time
from itertools import combinations, permutations
from collections import defaultdict
from copy import deepcopy
from functools import lru_cache

inp = [s.strip("\n") for s in open("input.txt")]


class Wire:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Wire(name: {self.name}, value:{self.value})"


class MyDefaultDict(defaultdict):
    """Taken from: https://stackoverflow.com/a/2912455/15598055"""

    def __missing__(self, key):
        if self.default_factory is None:
            return KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


# ----------common for both parts


# ----------part 1
class Gate1:
    def __init__(self, inp1: Wire, inp2: Wire, out: Wire, _type: str):
        self.inp1 = inp1
        self.inp2 = inp2
        self.out = out
        self._type = _type

    def process(self):
        a, b = self.inp1.value, self.inp2.value
        if a == -1 or b == -1:
            raise "Gate asked to process before inputs ready"
        match self._type:
            case "AND":
                return int(a == 1 and b == 1)
            case "OR":
                return int(a == 1 or b == 1)
            case "XOR":
                return int(a != b)

    def __repr__(self):
        a, b, out = self.inp1.value, self.inp2.value, self.out.value
        return f"Gate(type: {self._type}, a: {a}, b: {b}, out: {out})"


wires = MyDefaultDict(lambda k: Wire(k, -1))
not_processed: list[Gate1] = []

# wire starting values
for s in inp[: inp.index("")]:
    name, value = s.split(": ")
    wires[name].value = int(value)

# init gates
for s in inp[inp.index("") + 1 :]:
    inp1, _type, inp2, _, out = s.split(" ")
    not_processed.append(Gate1(wires[inp1], wires[inp2], wires[out], _type))

# simulate
while not_processed:
    for i in range(len(not_processed) - 1, -1, -1):
        g = not_processed[i]
        if g.inp1.value != -1 and g.inp2.value != -1:
            res = g.process()
            wires[g.out.name].value = res
            not_processed.pop(i)


z = [w for w in wires.values() if w.name.startswith("z")]
z.sort(key=lambda x: x.name, reverse=True)
bits = "".join([str(w.value) for w in z])
answer1 = int(f"0b{bits}", base=0)

print(f"Part 1 answer: {answer1}")
# ----------part 1
# 61886126253040


# ----------part 2
class Gate2:
    def __init__(self, inp1: Wire, inp2: Wire, out: Wire, _type: str):
        self.inp1 = inp1
        self.inp2 = inp2
        self.out = out
        self._type = _type

    def process(self):
        a, b = self.inp1.value, self.inp2.value
        if a is None or b is None:
            raise "Gate asked to process before inputs ready"

        return (a, self._type, b)
        # return f"({a} {self._type} {b})"

    def __repr__(self):
        a, b, out = self.inp1.value, self.inp2.value, self.out.value
        return f"Gate(type: {self._type}, a: {a}, b: {b}, out: {out})"

@lru_cache
def wire_replace(search, old, new):
    if isinstance(search, (tuple, list)) and (
        search == old or tuple(reversed(search)) == old
    ):
        return new
    if isinstance(search, (str, int)):
        return search
    return tuple([wire_replace(x, old, new) for x in search])

# cache wires and gate input parsing
wires_inp = []
for s in inp[: inp.index("")]:
    name, value = s.split(": ")
    if name.startswith("x") or name.startswith("y"):
        value = name
    wires_inp.append((name, value))
gate_inp = []
for s in inp[inp.index("") + 1 :]:
    inp1, _type, inp2, _, out = s.split(" ")
    if inp2.startswith("x"):
        inp1, inp2 = inp2, inp1
    gate_inp.append((inp1,inp2,_type,out))

@lru_cache
def simulate(switch: list, should_print=False):
    # wire starting values
    wires = MyDefaultDict(lambda k: Wire(k, None))
    for (name, value) in wires_inp:
        wires[name].value = value

    # init gates
    not_processed: list[Gate2] = []
    for (inp1, inp2,_type, out) in gate_inp:
        not_processed.append(Gate2(wires[inp1], wires[inp2], wires[out], _type))

    # switch
    for s in switch:
        g1, g2 = not_processed[s[0]], not_processed[s[1]]
        g1.out, g2.out = g2.out, g1.out

    # simulate
    while not_processed:
        did_something = False
        for i in range(len(not_processed) - 1, -1, -1):
            g = not_processed[i]
            if g.inp1.value is not None and g.inp2.value is not None:
                res = g.process()
                wires[g.out.name].value = res
                not_processed.pop(i)
                did_something = True
        if not did_something:
            raise "Infinite loop in simulation"

    # simplify results
    z: list[Wire] = [w for w in wires.values() if w.name.startswith("z")]
    z.sort(key=lambda x: x.name)
    for i in range(45, 0, -1):
        cur_w = z[i]
        prev_w = z[i - 1]
        to_rep = (prev_w.value[0], "AND", prev_w.value[-1])

        # replace prev carry
        cur_w.value = wire_replace(cur_w.value, to_rep, "carry_prev")

        # replace all simple carries (x0 and y0), (x1 and y1) etc.
        # for j in range(0, 45):
        j = i-1
        to_rep = (f"x{str(j).rjust(2, "0")}", "AND", f"y{str(j).rjust(2, "0")}")
        cur_w.value = wire_replace(cur_w.value, to_rep, "carry_and")
        
        # replace compound carries with simple carry
        to_rep = ("carry_prev", "OR", "carry_and")
        cur_w.value = wire_replace(cur_w.value, to_rep, "carry_compound")

        # sort
        if cur_w.value[0] in ("carry_compound", "carry_prev"):
            cur_w.value = tuple(reversed(cur_w.value))
    
    if should_print:
        for w in z:
            print()
            print(w.name)
            print(w.value)

    # find bad z's
    # bad_zs = []
    good_z_count = 0
    for i, w in enumerate(z):
        v = w.value
        xpad = f"x{str(i).rjust(2, "0")}"
        ypad = f"y{str(i).rjust(2, "0")}"
        if i == 0 and (xpad, "XOR", ypad) == v:
            good_z_count += 1
            continue
        if i==1 and ((xpad, "XOR", ypad), "XOR", "carry_prev") == v:
            good_z_count += 1
            continue
        if i == 45 and v == "carry_compound":
            good_z_count += 1
            continue
        if 1<=i<=44 and v == ((xpad, "XOR", ypad), "XOR", "carry_compound"):
            good_z_count += 1
            continue
        if should_print:
            print(f"bad {f"z{str(i).rjust(2, "0")}"}")
        # bad_zs.append((i, f"z{str(i).rjust(2, "0")}"))
    
    return good_z_count

gate_outs = []
for s in inp[inp.index("") + 1 :]:
    _, _, _, _, out = s.split(" ")
    gate_outs.append(out)
z_count = len([x for x in gate_outs if x.startswith("z")])

def find_last_two_pairs():
    switches = ((102, 106), (157, 190))
    yet_to_try = list(range(len(gate_outs)))
    for s in switches:
        for x in s:
            try:
                yet_to_try.remove(x)
            except:
                raise Exception(f"didn't find {x} in yet_to_find")
    good_count = simulate(switches, should_print=True)
    a, b = gate_outs.index("z24"), gate_outs.index("z32")


    mx_count = 0
    tries = 0
    for comb in combinations(yet_to_try, 2):
        tries += 1
        if tries < 15000:
            continue
        if tries % 1000 == 0:
            print(tries)
            print(f"mx count: {mx_count}")
        # comb1
        comb1 = ((a, comb[0]), (b, comb[1]))
        try:
            good_count = simulate((*switches, *comb1))
            mx_count = max(good_count, mx_count)
            if good_count == z_count:
                switches = (*switches, *comb1)
                break
        except:
            pass

        # comb2
        comb2 = ((a, comb[1]), (b, comb[0]))
        try:
            good_count = simulate((*switches, *comb2))
            mx_count = max(good_count, mx_count)
            if good_count == z_count:
                switches = (*switches, *comb1)
                break
        except:
            pass
    sys.exit()    

def find_first_two_pairs():
    switches = ()
    good_count = simulate(switches, should_print=True)
    print(f"switches: {switches}")
    yet_to_try = list(range(len(gate_outs)))
    comb_len = 2

    for s in switches:
        for x in s:
            try:
                yet_to_try.remove(x)
            except:
                pass


    while good_count != z_count:
        changed_something = False
        for comb in permutations(yet_to_try, comb_len):
            try_switch = [(comb[i], comb[i+1]) for i in range(0, len(comb)-1, 2)]
            
            try:
                new_good_count = simulate((*switches, *try_switch))
            except:
                continue
            
            if new_good_count > good_count:
                good_count = new_good_count
                switches = (*switches, *try_switch)
                simulate((*switches, *try_switch), should_print=True)
                changed_something = True
                time.sleep(5)
                break

            # if new_good_count == good_count-comb_len:
            if new_good_count < good_count:
                changed_something = True
                for s in try_switch:
                    yet_to_try.remove(s[0])
                    yet_to_try.remove(s[1])        
                break
            
        if not changed_something:
            break
    sys.exit()

# calculate final answer
switches = ((102, 106), (157, 190), (103, 116), (125, 132))
# switches = ()
flat_switches = []
for s in switches:
    flat_switches.extend(s)
names = [gate_outs[x] for x in flat_switches]
names.sort()
answer2 = ",".join(names)

print(f"Part 2 answer: {answer2}")
# ----------part 2
