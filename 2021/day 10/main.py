# read input
with open('input.txt') as f:
    syntax = [s.rstrip() for s in f.readlines()]
    
    
#----------part 1
# chars = '([{<)]}>'
# points = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
# ans = 0
# for line in syntax:
#     stack = []
#     for x in line:
#         idx = chars.index(x)
#         if idx < 4:
#             stack.append(x)
#         elif chars[idx-4] == stack[-1]:
#             del stack[-1]
#         else:
#             ans += points[x]
#             break
# print(ans)
#----------part 1


#----------part 2
chars = '([{<)]}>'
points = {')' : 1, ']' : 2, '}' : 3, '>' : 4}
scores = []
for line in syntax:
    stack = []
    for x in line:
        idx = chars.index(x)
        if idx < 4:
            stack.append(x)
        elif chars[idx-4] == stack[-1]:
            del stack[-1]
        else:
            break
    else:
        rem = ''.join(stack)
        rem = ''.join(reversed([chars[chars.index(x)+4] for x in rem]))
        score = 0
        for char in rem:
            score *= 5
            score += points[char]
        scores.append(score)

scores = sorted(scores)
ans = scores[len(scores)//2]
print(ans)
#----------part 2