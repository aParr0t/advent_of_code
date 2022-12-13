# read input
packets = [eval(s.rstrip("\n")) for s in open("input.txt") if s != "\n"]

# ----------both parts
def compare(a, b):
    # integer check
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return "correct"
        elif a > b:
            return "incorrect"
        elif a == b:
            return "continue"

    if isinstance(a, int):
        a = [a]

    if isinstance(b, int):
        b = [b]

    for (c, d) in zip(a, b):
        compare_result = compare(c, d)
        if compare_result == "correct":
            return "correct"
        elif compare_result == "incorrect":
            return "incorrect"
    a_len, b_len = len(a), len(b)
    if a_len < b_len:
        return "correct"
    elif b_len < a_len:
        return "incorrect"
    elif a_len == b_len:
        return "continue"


# ----------both parts

# ----------part 1
idx_sum = 0
for i in range(0, len(packets), 2):
    if compare(packets[i], packets[i + 1]) == "correct":
        idx_sum += i // 2 + 1

print(f"Part 1 answer: {idx_sum}")
# ----------part 1

# ----------part 2
# got help with quicksort from: https://www.youtube.com/watch?v=0SkOjNaO1XY
def partition_packets(packets, left, right):
    pivot = packets[right]
    pivot_idx = right
    i = left - 1
    for j in range(left, right):
        # modified the comparison from quicksort
        if compare(packets[j], pivot) == "correct":
            i += 1
            packets[i], packets[j] = packets[j], packets[i]
    packets[pivot_idx], packets[i + 1] = packets[i + 1], packets[pivot_idx]

    return i + 1


def sort_packets(packets, left=0, right=None):
    if right is None:
        right = len(packets) - 1
    if left >= right:
        return

    pivot_idx = partition_packets(packets, left, right)
    sort_packets(packets, left, pivot_idx - 1)
    sort_packets(packets, pivot_idx + 1, right)


# order packets using quicksort
div_packets = [[[2]], [[6]]]
packets.extend(div_packets)
sort_packets(packets)

# get the decoder key
decoder_key = 1
for div_packet in div_packets:
    decoder_key *= packets.index(div_packet) + 1

print(f"Part 2 answer: {decoder_key}")
# ----------part 2
