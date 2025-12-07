from collections import defaultdict
from functools import cache

Space = list(line.strip() for line in open("07.input").readlines())
S = Space[0].index("S")

Rays = defaultdict(set)
Rays[0] = {S}

P1 = 0
for row in range(1, len(Space)):
    for col in Rays[row - 1]:
        if Space[row][col] == ".":
            Rays[row].add(col)
        elif Space[row][col] == "^":
            P1 += 1
            if 0 <= col - 1 < len(Space[0]):
                Rays[row].add(col - 1)
            if 0 <= col + 1 < len(Space[0]):
                Rays[row].add(col + 1)
print(f"Part 1: {P1}")


# Part 2:
@cache
def possible_timelines(row, col):
    global Space
    if not 0 <= col < len(Space[0]):
        return 0
    elif row >= len(Space) - 1:
        return 1
    elif Space[row + 1][col] == ".":
        return possible_timelines(row + 1, col)
    elif Space[row + 1][col] == "^":
        return possible_timelines(row + 1, col - 1) + possible_timelines(row + 1, col + 1)


print(f"Part 2: {possible_timelines(0, S)}")
