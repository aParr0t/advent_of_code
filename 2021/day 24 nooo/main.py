# read input
with open('input.txt') as f:
    lines = [s.rstrip() for s in f.readlines()]

def validate(num: list):
    # later make the vals start with values from parmater
    vals = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    inp_idx = 0

    # later change the idx to go from parameter to len(lines)
    for idx in range(0, len(lines)):
        s = lines[idx]
        func = s[:3]
        a = s[4]
        b = None
        if func != 'inp':
            b = s[6:]
            if b in vals:
                b = vals[b]
            else:
                b = int(b)
        # parse and evaluate
        if func == 'inp':
            vals[a] = num[inp_idx]
            inp_idx += 1
        elif func == 'add':
            vals[a] += b
        elif func == 'mul':
            vals[a] *= b
        elif func == 'div':
            vals[a] = int(vals[a]/b)
        elif func == 'mod':
            vals[a] %= b
        elif func == 'eql':
            vals[a] = 1 if vals[a] == b else 0
    print(vals)
    return vals['z']

def increment(num: list):
    i = -1
    num[i] += 1
    while num[i] % 10 == 0:
        num[i] = 1
        i -= 1
        num[i] += 1
    return num

#----------part 1
guess = '71111591111111'.replace('0', '1')
guess = [int(x) for x in guess]
validate(guess)


# for i in range(0, len(lines), 18):
#     res = [ s[s.index(' ')+1:s.index(' ')+2] for s in lines[i:i+18] ]
#     print(res)
#----------part 1

#----------part 2

#----------part 2