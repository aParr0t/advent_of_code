# read input
with open('input.txt') as f:
    indata = []
    for line in f.readlines():
        indata.append(int(line.rstrip()))

#----------part 1
# count = sum([1 for i in range(1, len(indata)) if indata[i] > indata[i-1]])
# print(count)
#----------part 1

#----------part 2
# count = 0
# prev_window = None
# for i in range(len(indata)-2):
#     current_window = sum(indata[i:i+3])
#     if prev_window:
#         if current_window > prev_window:
#             count += 1

#     prev_window = sum(indata[i:i+3])

# print(count)
#----------part 2