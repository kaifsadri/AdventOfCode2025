puzzle_input = [l.strip() for l in open("01.input").readlines()]

p1 = 0
p2 = 0
pos = 50
c = 0
for line in puzzle_input:
    d, n = line[0], int(line[1:])
    crossings, n = divmod(n, 100)  # crossings caused by the number of full rotations
    if d == "L":
        if pos > 0 and n > pos:  # this condition produces one more crossing
            crossings += 1
        pos = (pos - n) % 100
    else:
        if n + pos > 100:  # this condition produces one more crossing
            crossings += 1
        pos = (pos + n) % 100
    if pos == 0:
        p1 += 1
    p2 += crossings

print(f"Part 1: {p1}")
print(f"Part 2: {p2+p1}")
