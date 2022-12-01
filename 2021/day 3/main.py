# read input
with open('input.txt') as f:
    indata = list(map(
        lambda x: x.rstrip(),
        f.readlines()
        ))

#----------part 1
# row_len = len(indata[0])
# col_len = len(indata)
# count = [0] * row_len

# # count the 1s and 0s
# for i in range(row_len):
#     count[i] = len(list(filter(lambda x: x[i] == '1', indata)))
#     count[i] = '1' if count[i] > col_len-count[i] else '0'  # most common bit

# gamma = ''.join(count)
# epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])  # flip bits
# power = int(gamma, 2) * int(epsilon, 2)
# print(power)
#----------part 1


#----------part 2
row_len = len(indata[0])
count = [0] * row_len

oxygen = indata.copy()
co2 = indata.copy()
for j in range(row_len):
    if len(oxygen) != 1:
        for i in range(row_len):
            count[i] = len(list(filter(lambda x: x[i] == '1', oxygen)))
            count[i] = '1' if count[i] >= len(oxygen)-count[i] else '0'  # most common bit
        oxygen = list(filter(lambda x: x[j] == count[j], oxygen))
    
    if len(co2) != 1:
        for i in range(row_len):
            count[i] = len(list(filter(lambda x: x[i] == '1', co2)))
            count[i] = '0' if count[i] >= len(co2)-count[i] else '1'  # most common bit
        co2 = list(filter(lambda x: x[j] == count[j], co2))

life = int(oxygen[0], 2) * int(co2[0], 2)
print(life)
#----------part 2