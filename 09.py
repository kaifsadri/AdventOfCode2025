Points = list(tuple(map(int, line.split(","))) for line in open("09.input").readlines())
Areas = dict()  # hold the areas, used in part 2 to make things faster

P1 = 0
for n, (x1, y1) in enumerate(Points):
    for x2, y2 in Points[n + 1 :]:
        A = (1 + abs(x1 - x2)) * (1 + abs(y1 - y2))
        Areas[A] = (x1, y1, x2, y2)
        if A > P1:
            P1 = A
print(f"Part 1: {P1}")


# Plan for P2: Find the boundary of the area covereg by red/green tiles,
# and find the frontier around it. Then when checking the rectangles, make sure none
# of its edges has a commpon point with this boundary.
# Note: Many online 'fast' solutions only check for boundaries intersecting with the rectangle.
# It is possible to have a rectangle that is outside the area but has no intersecting edges with the area.
Boundary = set()  # set including all the red and green tiles
for n, (x1, y1) in enumerate(Points):
    try:
        x2, y2 = Points[n + 1]
    except IndexError:
        x2, y2 = Points[0]
    if x1 == x2:
        for t in range((m := min(y1, y2)), max(y1, y2) + 1):
            Boundary.add((x1, t))
    elif y1 == y2:
        for t in range((m := min(x1, x2)), max(x1, x2) + 1):
            Boundary.add((t, y1))
    else:
        raise ValueError(f"Incompatible pair of points: ({x1}, {y1}) and ({x2}, {y2})")

# Plan for P2: Build a set, denoting all the points on the OUTSIDE layer of the boundary, one point thick
minx = min(p[0] for p in Points)
p1, p2 = [p for p in Points if p[0] == minx]
# now select starting point to the left of this, in the middle
# we will fill the frontier
StartingPoint = (minx - 1, (p1[1] + p2[1]) // 2)
ToGo = {StartingPoint}
Frontier = set()
D = set((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)) - {(0, 0)}
while ToGo:
    p = ToGo.pop()
    Frontier.add(p)
    for d in D:
        np = (p[0] + d[0], p[1] + d[1])
        if (
            np not in Frontier
            and np not in Boundary
            and any((np[0] + k[0], np[1] + k[1]) in Boundary for k in D)
        ):
            ToGo.add(np)

P2 = 0
for a in sorted(Areas, reverse=True):
    x1, y1, x2, y2 = Areas[a]
    try:
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            if (x, y1) in Frontier or (x, y2) in Frontier:
                raise Exception()
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            if (x1, y) in Frontier or (x2, y) in Frontier:
                raise Exception()
        print(f"Part 2: {a}")
        break
    except Exception:
        continue
