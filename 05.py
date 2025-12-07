P = list(line.strip() for line in open("05.input").readlines() if line.strip())
# Part 1
R = set()
In = set()
F = set()
for line in P:
    if "-" in line:
        lo, hi = line.split("-")
        R.add((int(lo), int(hi)))
    else:
        In.add(int(line))
for ing in In:
    for r in R:
        if r[0] <= ing <= r[1]:
            F.add(ing)
            break  # fresh once, fresh always!
print(f"Part 1: {len(F)}")

# Part 2:
R = sorted(R, key=lambda x: x[0])
P2 = 0
lo, hi = R[0]
for ll, hh in R[1:]:
    if ll <= hi:  # Overlap
        hi = max(hh, hi)
    else:  # No overlap
        P2 += hi - lo + 1
        lo, hi = ll, hh
P2 += hi - lo + 1  # take care of last range
print(f"Part 2: {P2}")
