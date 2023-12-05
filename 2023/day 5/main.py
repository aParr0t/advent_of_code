# read input
inp = [s.rstrip() for s in open("input.txt")]


class Range:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.dest_start = dest_start
        self.source_start = source_start
        self.length = length

    def __repr__(self) -> str:
        return f"Range(dest_start: {self.dest_start}, source_start: {self.source_start}, length: {self.length})"

    def convert(self, source: int):
        if self.source_start <= source < self.source_start + self.length:
            offset = source - self.source_start
            res = self.dest_start + offset
            return res
        else:
            return source


class Table:
    def __init__(self, from_name: str, to_name: str):
        self.from_name = from_name
        self.to_name = to_name
        self.ranges: list[Range] = []

    def add_range(self, dest_start: int, source_start: int, length: int):
        self.ranges.append(Range(dest_start, source_start, length))

    def filter(self, _numbers: list[int]):
        to_convert = [*_numbers]
        numbers = []
        for r in self.ranges:
            for i in range(len(to_convert) - 1, -1, -1):
                n = to_convert[i]
                res = r.convert(n)
                if res != n:
                    to_convert.pop(i)
                    numbers.append(res)
        numbers.extend(to_convert)
        return numbers


seeds = inp[0][inp[0].index(":") + 2 :].split(" ")
seeds = [int(s) for s in seeds]

table_strings = "\n".join(inp[2:]).split("\n\n")
tables: list[Table] = []
for table_string in table_strings:
    lines = table_string.split("\n")
    name_string = lines[0][: lines[0].index(" map")].split("-")
    from_name, _, to_name = name_string
    table = Table(from_name, to_name)
    for range_string in lines[1:]:
        dest_start, source_start, length = [int(s) for s in range_string.split(" ")]
        table.add_range(dest_start, source_start, length)
    tables.append(table)

# ----------part 1
numbers = [*seeds]
for table in tables:
    numbers = table.filter(numbers)

lowest_location = min(numbers)
print(f"Part 1 answer: {lowest_location}")
# ----------part 1


# ----------part 2
def backwards(numbers):
    _numbers = [*numbers]
    for i in range(len(tables) - 1, -1, -1):
        table = tables[i]
        converted = [False for _ in _numbers]
        for r in table.ranges:
            for i, n in enumerate(_numbers):
                if r.dest_start <= n < r.dest_start + r.length:
                    offset = n - r.dest_start
                    res = r.source_start + offset
                    if converted[i] == False:
                        _numbers[i] = res
                        converted[i] = True
    return _numbers


# finding all the boundaries. The answer seed will be between one of these boundaries
boundaries = set()
seed_ranges = []
for i in range(0, len(seeds), 2):
    start, length = seeds[i], seeds[i + 1]
    seed_ranges.append(range(start, start + length))
    boundaries.update([start, start + length])
for table in tables:
    for r in table.ranges:
        left = r.dest_start
        right = r.dest_start + r.length
        boundaries.update([left, right])
boundaries = sorted(boundaries)

# finding the seeds of the boundaries
possible_seed_boundaries = backwards(boundaries)

# finding the range of the answer-seeds
actually_possible = []
for i, s in enumerate(possible_seed_boundaries):
    is_possible = False
    for r in seed_ranges:
        if s in r:
            is_possible = True
            break
    if not is_possible:
        continue

    # the -1 and +1 is the magic. Neccessary because there's a possibility
    # that the border is the answer
    boundary_start, boundary_end = boundaries[i - 1] - 1, boundaries[i] + 1
    break

# calculating seeds in the range of the answer. The answer-seed will be among these
answer_seeds = backwards(list(range(boundary_start, boundary_end)))

# finding smallest (first in list) valid seed that will give the lowest location
for s in answer_seeds:
    is_possible = False
    for r in seed_ranges:
        if s in r:
            is_possible = True
            break
    if not is_possible:
        continue

    answer_seed = s
    break

# Calculating lowest location
numbers = [answer_seed]
for table in tables:
    numbers = table.filter(numbers)
lowest_location = numbers[0]

print(f"Part 2 answer: {lowest_location}")
# ----------part 2
