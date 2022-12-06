# read input
signal = open("input.txt").readline().rstrip()

# ----------both parts
# the solve() is almost identical to the famous task of finding
# the longest unique substring in a string.
def solve(signal, packet_length):
    """returns number of chars visited before finding the first packet with length packet_length"""
    visited = {}
    i = 0
    for j in range(len(signal)):
        char = signal[j]
        if char in visited and visited[char] >= i:
            i = visited[char] + 1
        if j - i + 1 == packet_length:
            chars_visited = j + 1
            break
        visited[char] = j
        j += 1
    return chars_visited


# ----------both parts

# ----------part 1
chars_visited = solve(packet_length=4, signal=signal)
print(f"Part 1 answer: {chars_visited}")
# ----------part 1

# ----------part 2
chars_visited = solve(packet_length=14, signal=signal)
print(f"Part 2 answer: {chars_visited}")
# ----------part 2
