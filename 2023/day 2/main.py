# read input
inp = [s.rstrip() for s in open("input.txt")]


# ----------part 1
class CubeSet:
    possible = {"red": 12, "green": 13, "blue": 14}

    def __init__(self, cubes: dict):
        self.cubes = cubes

    @classmethod
    def from_string(cls, s: str):
        cubes = {}
        for cube in s.split(", "):
            sep = cube.index(" ")
            count = int(cube[:sep])
            color = cube[sep + 1 :]
            cubes[color] = count
        return cls(cubes)

    def __repr__(self):
        return f"Set({self.cubes})"

    def is_valid(self):
        for color, count in self.cubes.items():
            if count > CubeSet.possible[color]:
                return False
        return True


class Game:
    def __init__(self, id: int, cube_sets: list[CubeSet]):
        self.id = id
        self.cube_sets = cube_sets

    @classmethod
    def from_string(cls, s: str):
        sep = s.find(":")
        id = int(s[5:sep])
        sets_string = s[sep + 2 :]
        cube_sets = []
        for set_string in sets_string.split("; "):
            cube_sets.append(CubeSet.from_string(set_string))
        return cls(id, cube_sets)

    def __repr__(self):
        return f"Game(id: {self.id}, sets: {self.cube_sets})"

    def is_possible(self):
        return all([c.is_valid() for c in self.cube_sets])

    def minimum(self):
        cubes = CubeSet({"red": 0, "green": 0, "blue": 0})
        for cube_set in self.cube_sets:
            for color, count in cube_set.cubes.items():
                cubes.cubes[color] = max(cubes.cubes[color], count)
        return cubes


res = 0
for s in inp:
    game = Game.from_string(s)
    if game.is_possible():
        res += game.id

print(f"Part 1 answer: {res}")
# ----------part 1

# ----------part 2
res = 0
for s in inp:
    game = Game.from_string(s)
    minimum = game.minimum()
    power = 1
    for count in minimum.cubes.values():
        power *= count
    res += power

print(f"Part 2 answer: {res}")
# ----------part 2
