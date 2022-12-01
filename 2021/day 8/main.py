# read input
with open('input.txt') as f:
    entries = []
    for s in f.readlines():
        s = s.strip()
        signals = s[:s.index('|')-1].split(' ')
        out = s[s.index('|')+2:].split(' ')
        entries.append({
            'signals' : signals,
            'out' : out
        })

#----------part 1
# ans = sum([sum([1 for s in x['out'] if len(s) in [2, 3, 4, 7]]) for x in entries])  # ugly solution
# ans = 0
# for entry in entries:
#     count = sum([1 for s in entry['out'] if len(s) in [2, 3, 4, 7]])
#     ans += count
# print(ans)
#----------part 1

#----------part 2
ans = 0
digits = [0] * 10
for entry in entries:
    signals = entry['signals']
    # decode 1, 4, 7, 8
    digits[1] = [x for x in signals if len(x)==2][0]
    digits[4] = [x for x in signals if len(x)==4][0]
    digits[7] = [x for x in signals if len(x)==3][0]
    digits[8] = [x for x in signals if len(x)==7][0]

    def match(strings, template, goal):
        for s in strings:
            if sum([1 for l in template if l in s]) == goal:
                return s
        return -1

    nums = [x for x in signals if len(x)==6]  # decode 0, 6, 9
    digits[6] = match(nums, digits[1], 1)
    digits[9] = match(nums, digits[4], 4)
    digits[0] = [ x for x in nums if x not in (digits[6], digits[9]) ][0]
    nums = [x for x in signals if len(x)==5]  # decode 2, 3, 5
    digits[2] = match(nums, digits[4], 2)
    digits[3] = match(nums, digits[1], 2)
    digits[5] = [ x for x in nums if x not in (digits[2], digits[3]) ][0]

    # decode final display
    value = ''
    for signal in entry['out']:
        signal_set = set(signal)
        true_signal = [x for x in digits if set(x)==signal_set][0]
        value += str(digits.index(true_signal))
    ans += int(value)

print(ans)
#----------part 2