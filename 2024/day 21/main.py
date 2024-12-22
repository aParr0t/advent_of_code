# ----------common for both parts
from itertools import permutations, product

codes = [s.strip("\n") for s in open("input.txt")]

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
num_pos = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
    " ": (0, 3),
}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
dir_pos = {"^": (1, 0), "A": (2, 0), "<": (0, 1), "v": (1, 1), ">": (2, 1), " ": (0, 0)}


def code_to_direction(code: str, start=num_pos["A"]):
    cur_pos = start
    stages = []
    for nxt in code:
        nxt_pos = num_pos[nxt]
        dx, dy = nxt_pos[0] - cur_pos[0], nxt_pos[1] - cur_pos[1]
        stage = ""
        if dx > 0:
            stage += ">" * abs(dx)
        if dy < 0:
            stage += "^" * abs(dy)
        if dx < 0:
            stage += "<" * abs(dx)
        if dy > 0:
            stage += "v" * abs(dy)
        stages.append(stage)
        cur_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
    return "A".join(stages) + "A"


def code_to_direction1(code: str):
    cur_pos = (2, 3)
    stages = []
    for nxt in code:
        nxt_pos = num_pos[nxt]
        dx, dy = nxt_pos[0] - cur_pos[0], nxt_pos[1] - cur_pos[1]
        stage = ""
        if dx > 0:
            stage += ">" * abs(dx)
        if dy < 0:
            stage += "^" * abs(dy)
        if dx < 0:
            stage += "<" * abs(dx)
        if dy > 0:
            stage += "v" * abs(dy)
        stages.append(stage)
        cur_pos = (cur_pos[0] + dx, cur_pos[1] + dy)

    all_stage_perm_strs = []
    for s in stages:
        stage_perm = set(permutations(s))
        stage_perm_strs = ["".join(p) for p in stage_perm]
        all_stage_perm_strs.append(stage_perm_strs)

    all_dirs_lists = product(*all_stage_perm_strs)
    all_dirs = ["A".join(l) + "A" for l in all_dirs_lists]

    return all_dirs


def dir_to_dir(_dir_str: str, start=dir_pos["A"]):
    cur_pos = start
    dir_str = ""
    for nxt in _dir_str:
        nxt_pos = dir_pos[nxt]
        dx, dy = nxt_pos[0] - cur_pos[0], nxt_pos[1] - cur_pos[1]
        if dy > 0:
            dir_str += "v" * abs(dy)
        if dx > 0:
            dir_str += ">" * abs(dx)
        if dy < 0:
            dir_str += "^" * abs(dy)
        if dx < 0:
            dir_str += "<" * abs(dx)
        dir_str += "A"
        cur_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
    return dir_str


def robot_action(robots, idx: int, action: str, ci=-1):
    r = robots[idx]
    _type = r[2]
    # robot: [x, y, type]
    match action:
        case ">":
            r[0] += 1
        case "<":
            r[0] -= 1
        case "^":
            r[1] -= 1
        case "v":
            r[1] += 1
        case "A":
            if _type == "num":
                a = next((k for k, v in num_pos.items() if v == (r[0], r[1])))
                # print(f"numeric robot pressed {a} at {ci}")
                return
            elif _type == "dir":
                a = next((k for k, v in dir_pos.items() if v == (r[0], r[1])))
            else:
                raise "wtf is the type"

            if a is None:
                raise "how the fck is there no type"

            robot_action(robots, idx - 1, a, ci)


def setup_robots(count: int):
    robots = [[*num_pos["A"], "num"]]
    for _ in range(count):
        robots.append([*dir_pos["A"], "dir"])
    return robots


def is_valid(s: str, count: int):
    """Checks if the instructions are valid"""
    robots = setup_robots(count)
    for ci, c in enumerate(s):
        robot_action(robots, len(robots) - 1, c, ci)
        for r in robots:
            if r[2] == "num" and (r[0], r[1]) == num_pos[" "]:
                return False
            if r[2] == "dir" and (r[0], r[1]) == dir_pos[" "]:
                return False
    return True


def visualize(instructions: str):
    robots = setup_robots(2)
    # robots = [[*num_pos["A"], "num"], [*dir_pos["A"], "dir"], [*dir_pos["A"], "dir"]]
    for ci, c in enumerate(instructions):
        print()
        robot_action(robots, len(robots) - 1, c, ci)
        print(f"instruction {c}")
        # visualize the robots
        for ridx, r in enumerate(robots):
            print(f"idx: {ridx}, type: {r[2]}")
            if r[2] == "num":
                w, h = 3, 4
            else:
                w, h = 3, 2
            for y in range(h):
                for x in range(w):
                    if (x, y) == (r[0], r[1]):
                        print("#", end="")
                    else:
                        print(".", end="")
                print()
        input()


def is_instr_valid(s: str, start: tuple, bad: tuple):
    x, y = start
    for c in s:
        match c:
            case "v":
                y += 1
            case "^":
                y -= 1
            case ">":
                x += 1
            case "<":
                x -= 1
        if (x, y) == bad:
            return False
    return True


# ----------common for both parts

# ----------part 1
total = 0
for code in codes:
    dirs = code_to_direction1(code)
    min_d3 = ""
    for d in dirs:
        dir2 = dir_to_dir(d)
        dir3 = dir_to_dir(dir2)
        if is_valid(dir3, 2) and (min_d3 == "" or len(dir3) < len(min_d3)):
            min_d3 = dir3
    num = int("".join([x for x in code if x.isdigit()]))
    total += len(min_d3) * num

print(f"Part 1 answer: {total}")
# ----------part 1


# ----------part 2
# find best dir moves
dir_keys = list(dir_pos.keys())
dir_keys.remove(" ")
all_combs = ["".join(x) for x in product(dir_keys, repeat=2)]
best_dir = {}
for comb in all_combs:
    D = dir_to_dir(comb[1], dir_pos[comb[0]])
    perm = set(permutations(D))
    perm_strs = ["".join(p) for p in perm]
    best_d = ""
    best_D = ""
    for _d in perm_strs:
        if not _d.endswith("A"):
            continue
        if not is_instr_valid(_d, dir_pos[comb[0]], dir_pos[" "]):
            continue
        d = dir_to_dir(_d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        if best_d == "" or len(d) < len(best_d):
            best_d = d
            best_D = _d

    best_dir[comb] = best_D

# find best num moves
num_keys = list(num_pos.keys())
num_keys.remove(" ")
all_combs = ["".join(x) for x in product(num_keys, repeat=2)]
best_num = {}
for comb in all_combs:
    D = code_to_direction(comb[1], num_pos[comb[0]])
    perm = set(permutations(D))
    perm_strs = ["".join(p) for p in perm]
    best_d = ""
    best_D = ""
    for _d in perm_strs:
        if not _d.endswith("A"):
            continue
        if not is_instr_valid(_d, num_pos[comb[0]], num_pos[" "]):
            continue
        d = dir_to_dir(_d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        d = dir_to_dir(d)
        # if comb == "37":
        #     print(_d, d)
        if best_d == "" or len(d) < len(best_d):
            best_d = d
            best_D = _d

    best_num[comb] = best_D


# ^  <   ^   <   ^   A  >  AvvvA>A
# <A v<A >^A v<A >^A >A vA ^Av<AAA>^AvA^A

# ^<^<^A>AvvvA>A
# <Av<A>^Av<A>^A>AvA^Av<AAA>^AvA^A

from functools import lru_cache


@lru_cache
def slen(p: str, depth):
    # d = dir_to_dir(p[1], dir_pos[p[0]])
    d = best_dir[p]
    if depth == 0:
        return len(d)
    d = "A" + d
    pairs = [d[i] + d[i + 1] for i in range(0, len(d) - 1, 1)]
    tot = sum((slen(pr, depth=depth - 1) for pr in pairs))
    return tot


total = 0
keypad_count = 25
for code in codes:
    # print()
    # print(f"code {code}")
    code = "A" + code
    pairs = [code[i] + code[i + 1] for i in range(0, len(code) - 1, 1)]
    way = "".join([best_num[p] for p in pairs])
    # print(way)
    d = "A" + way
    pairs = [d[i] + d[i + 1] for i in range(0, len(d) - 1, 1)]
    ln = sum((slen(pr, depth=keypad_count - 1) for pr in pairs))
    num = int("".join([x for x in code if x.isdigit()]))
    # print(ln, num)
    total += ln * num


print(f"Part 2 answer: {total}")
# ----------part 2
# 453738142142564 too high
# 246778413153978 too high
# 125512212115646 too low

# total = 0
# keypad_count = 2
# for code in codes[:]:
#     print()
#     print(f"code {code}")
#     dirs = code_to_direction(code)
#     min_last_d = ""
#     for _d in dirs:
#         d = _d

#         if not is_num_valid(d):
#             continue
#         print(d)
#         for n in range(keypad_count):
#             d = dir_to_dir(d)
#             print(d)
#             import sys

#             sys.exit()
#         if min_last_d == "" or len(d) < len(min_last_d):
#             min_last_d = d
#     num = int("".join([x for x in code if x.isdigit()]))
#     print(len(min_last_d), num)
#     total += len(min_last_d) * num
