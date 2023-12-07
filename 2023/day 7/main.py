# read input
inp = [s.rstrip() for s in open("input.txt")]


class Card:
    strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, deck: str, bid: int):
        self.deck = deck
        self.bid = bid
        self.type = self.get_type()
        self.string = self.get_string()
        self.joker_type = self.get_joker_type()

    def get_type(self, deck=None):
        deck = deck or self.deck
        CS = set(deck)
        length = len(CS)
        if length == 1:
            return 7
        if length == 2:
            if deck.count(deck[0]) in [1, 4]:
                return 6
            else:
                return 5
        if length == 3:
            if any([deck.count(c) == 3 for c in deck]):
                return 4
            else:
                return 3
        if length == 4:
            return 2
        if length == 5:
            return 1

    def get_joker_type(self):
        if "J" not in self.deck or self.deck == "JJJJJ":
            return self.get_type()

        counts = {c: self.deck.count(c) for c in self.deck if c != "J"}
        max_c = max(counts.items(), key=lambda x: x[1])[0]

        d = self.deck.replace("J", max_c)
        return self.get_type(d)

    def get_string(self):
        return "".join([chr(97 + Card.strength.index(c)) for c in self.deck])


# ----------part 1
cards: list[Card] = []
for l in inp:
    d, b = l.split()
    b = int(b)
    cards.append(Card(d, b))
cards: list[Card] = sorted(cards, key=lambda x: x.type)
groups = [[cards[0]]]
for i, card in enumerate(cards[1:], 1):
    if card.type != cards[i - 1].type:
        groups.append([])
    groups[-1].append(card)

for g in groups:
    g.sort(key=lambda x: x.string)
    g.reverse()

flat: list[Card] = []
for g in groups:
    flat.extend(g)

res = 0
for i, c in enumerate(flat, 1):
    res += c.bid * i

print(f"Part 1 answer: {res}")
# ----------part 1


# ----------part 2
Card.strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

cards: list[Card] = []
for l in inp:
    d, b = l.split()
    b = int(b)
    cards.append(Card(d, b))

cards: list[Card] = sorted(cards, key=lambda x: x.joker_type)
groups = [[cards[0]]]
for i, card in enumerate(cards[1:], 1):
    if card.joker_type != cards[i - 1].joker_type:
        groups.append([])
    groups[-1].append(card)

for g in groups:
    g.sort(key=lambda x: x.string)
    g.reverse()

flat: list[Card] = []
for g in groups:
    flat.extend(g)

res = 0
for i, c in enumerate(flat, 1):
    res += c.bid * i

print(f"Part 2 answer: {res}")
# ----------part 2
