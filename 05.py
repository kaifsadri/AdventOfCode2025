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
            break # fresh once, fresh always!
print(f"Part 1: {len(F)}")

# Part 2:
L = sorted(R, key=lambda x: x[0], reverse=True)
M = set()
lo, hi = L.pop()
while L:
    ll, hh = L.pop()
    if lo <= ll <= hi:
        if lo <= hh <= hi:
            # this pair is useless. Ignore it:
            continue
        else:
            # produce a larger overlap set and continue
            hi = hh
            continue
    # if we are here, we have a cleaned-up range to add to tne list of answers
    M.add((lo, hi))
    lo, hi = ll, hh
M.add((lo, hi)) # take care of last pair
print(f"Part 2: {sum(hi - lo + 1 for lo, hi in M)}")
