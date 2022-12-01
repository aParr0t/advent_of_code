# read input
with open('input.txt') as f:
    indata = [x.rstrip() for x in f.readlines()]
    template = indata[0]
    pairs = {s[:2]: s[6] for s in indata[2:]}

#----------part 1
# for x in range(10):
#     idx = 1
#     while idx < len(template):
#         pair = template[idx-1:idx+1]
#         template = template[:idx] + pairs[pair] + template[idx:]
#         idx += 2

# chars = set(list(template))
# counts = [{'char': char, 'count': template.count(char)} for char in chars]
# common = sorted(counts, key=lambda x: x['count'])
# print(common[-1]['count'] - common[0]['count'])
#----------part 1


#----------part 2
pairs = {s[:2]: s[0]+s[6]+s[1] for s in indata[2:]}

noVal = -1
steps = 40
counts = {key: [noVal for x in range(steps)] for key in pairs.keys()}

def merge_counts(counts_1: dict, counts_2: dict, sub: str):
    res = counts_1.copy()
    for key, val in counts_2.items():
        if key in res:
            res[key] += val
        else:
            res[key] = val
    if sub != None:
        res[sub] -= 1
    return res

def search(s: str, depth: int):
    if depth == 0:
        chars = set(s)
        return {c: s.count(c) for c in chars}
    
    if counts[s][depth-1] != noVal:
        return counts[s][depth-1]

    new_str = pairs[s]
    a = search(new_str[:2], depth-1)
    b = search(new_str[1:], depth-1)
    counts[s][depth-1] = merge_counts(a, b, new_str[1])
    return counts[s][depth-1]

next_sub = None
total_counts = {}
for i in range(len(template)-1):
    pair = template[i:i+2]
    res = search(pair, steps)
    total_counts = merge_counts(total_counts, res, next_sub)
    next_sub = pair[1]

max_val = max(total_counts.values())
min_val = min(total_counts.values())
print(f'{max_val} - {min_val} = {max_val - min_val}')
#----------part 2