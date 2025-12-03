puzz = [line.strip() for line in open("03.input").readlines()]

P1 = 0
for line in puzz:
    ans = ""
    for t in [1, 0]:
        m = max(line[: len(line) - t])
        ans += m
        line = line[line.find(m) + 1 :]
    P1 += int(ans)
print(f"Part 1: {P1}")

P2 = 0
for line in puzz:
    ans = ""
    for t in range(11, -1, -1):
        m = max(line[: len(line) - t])
        ans += m
        line = line[line.find(m) + 1 :]
    P2 += int(ans)
print(f"Part 2: {P2}")
