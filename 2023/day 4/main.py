# read input
inp = [s.rstrip() for s in open("input.txt")]


def num_split(s: str):
    return [int(n) for n in s.split(" ") if n.isdigit()]


win_counts = []
for l in inp:
    sep = l.index("|")
    win_string = l[l.index(":") + 2 : sep - 1]
    numbers_string = l[sep + 2 :]
    win_numbers = set(num_split(win_string))
    numbers = set(num_split(numbers_string))
    winners = win_numbers.intersection(numbers)
    win_counts.append(len(winners))


# ----------part 1
points = 0
for win_count in win_counts:
    if win_count > 0:
        score = 2 ** (win_count - 1)
        points += score


print(f"Part 1 answer: {points}")
# ----------part 1


# ----------part 2
cards = [1 for _ in range(len(inp))]


for i, win_count in enumerate(win_counts):
    add = cards[i]
    for j in range(i + 1, i + win_count + 1):
        cards[j] += add

num_of_cards = sum(cards)

print(f"Part 2 answer: {num_of_cards}")
# ----------part 2
