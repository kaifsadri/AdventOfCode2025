L = list(line.strip() for line in open("04.input").readlines())

G = set()
for row, line in enumerate(L):
    for col, char in enumerate(line):
        if char == "@":
            G.add(row + col * 1j)
# Part 1
D = [
    -1 - 1j,
    -1 + 0j,
    -1 + 1j,
    0 + 1j,
    0 - 1j,
    1 + 1j,
    1 + 0j,
    1 - 1j,
]
R = set()
for r in G:
    if sum((r + t) in G for t in D) < 4:
        R.add(r)
print(f"Part 1: {len(R)}")

# Continue for Part 2
keep_going = True
while keep_going:
    keep_going = False
    for r in G:
        if r not in R and sum(((r + t) in G and (r + t) not in R) for t in D) < 4:
            R.add(r)
            keep_going = True
print(f"Part 2: {len(R)}")
