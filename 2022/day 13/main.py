from functools import cmp_to_key

# read input
packets = [eval(s.rstrip("\n")) for s in open("input.txt") if s != "\n"]

# ----------both parts
def compare(a, b):
    # integer check
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    for (c, d) in zip(a, b):
        compare_result = compare(c, d)
        if compare_result == -1:
            return -1
        elif compare_result == 1:
            return 1
    a_len, b_len = len(a), len(b)
    if a_len < b_len:
        return -1
    elif b_len < a_len:
        return 1
    else:
        return 0


# ----------both parts

# ----------part 1
idx_sum = 0
for i in range(0, len(packets), 2):
    if compare(packets[i], packets[i + 1]) == -1:
        idx_sum += i // 2 + 1

print(f"Part 1 answer: {idx_sum}")
# ----------part 1

# ----------part 2
# this commit uses cmp_to_key from functools
# so the built-in sort() can use my custom compare function
div_packets = [[[2]], [[6]]]
packets.extend(div_packets)
packets.sort(key=cmp_to_key(compare))

# get the decoder key
decoder_key = 1
for div_packet in div_packets:
    decoder_key *= packets.index(div_packet) + 1

print(f"Part 2 answer: {decoder_key}")
# ----------part 2
