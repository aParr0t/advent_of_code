# read input
with open('input.txt') as f:
    homework = [eval(s.rstrip()) for s in f.readlines()]

import math
def explode_str(s: str, area: list):
    i, i2 = area
    num_0 = int(s[i+1:s.index(',', i)])
    num_1 = int(s[s.index(',', i)+1:i2])

    # find the right number
    x1 = i2
    while s[x1] in '[,]' and x1 < len(s)-1: x1 += 1
    x2 = x1
    while s[x2] not in '[,]' and x2 < len(s)-1: x2 += 1
    right_num = s[x1:x2]
    if right_num:
        s = s[:x1] + str(int(right_num)+num_1) + s[x2:]
    
    # find the left number
    x2 = i
    while s[x2] in '[,]' and x2 > 0: x2 -= 1
    x1 = x2
    while s[x1] not in '[,]' and x1 > 0: x1 -= 1
    left_num = s[x1+1:x2+1]

    # replace pair with 0
    s = s[:i] + '0' + s[i2+1:]
    
    # replace the left number
    if left_num:
        s = s[:x1+1] + str(int(left_num)+num_0) + s[x2+1:]
    return s

def get_nested_pair(s: str):
    i = 0
    depth = 0
    jumps = 0
    while i < len(s):
        if s[i] == '[':
            depth += 1
        elif s[i] == ']':
            depth -= 1
            jumps += 1
        
        if depth == 5:
            i2 = s.index(']', i)
            return i, i2

        i += 1
    return -1

def split_in_str(s: str):
    x1 = 0
    while x1 < len(s):
        while s[x1] in '[,]' and x1 < len(s)-1: x1 += 1
        x2 = x1
        while s[x2] not in '[,]' and x2 < len(s)-1: x2 += 1
        num = s[x1:x2]
        if len(num) == 0:
            break
        num = int(num)
        if num >= 10:
            inj = f'[{math.floor(num/2)},{math.ceil(num/2)}]'
            s = s[:x1] + inj + s[x2:]
            return s, True
        else:
            x1 = x2
    return s, False 
    
def add(a: list, b: list):
    res = [a, b]
    res_str = str(res).replace(' ', '')
    while True:
        pair = get_nested_pair(res_str)
        if pair != -1:
            res_str = explode_str(res_str, pair)
            continue
        res_str, success = split_in_str(res_str)
        if success:
            continue
        break
    return res_str

def magnitude(x):
    if isinstance(x, int):
        return x
    
    return magnitude(x[0])*3 + magnitude(x[1])*2

#----------part 1
# a = homework[0]
# for i in range(1, len(homework)):
#     b = homework[i]
#     a = add(a, b)
#     a = eval(a)

# mag = magnitude(a)
# print(mag)
#----------part 1

#----------part 2 Brute fking force
largest_mag = 0
for x in range(len(homework)-1):
    for y in range(x+1, len(homework)):
        a, b = homework[x], homework[y]
        # one way
        res = eval(add(a, b))
        mag = magnitude(res)
        largest_mag = max(largest_mag, mag)
        # the other way
        res = eval(add(b, a))
        mag = magnitude(res)
        largest_mag = max(largest_mag, mag)
print(largest_mag)
#----------part 2