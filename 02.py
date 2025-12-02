puzz = [list(map(int, l.split("-"))) for l in open("02.input").readline().strip().split(",")]


def invalid1(n: int) -> bool:
    s = str(n)
    if len(s) == 0 or len(s) % 2:
        return False
    t = len(s) // 2
    if s[0:t] == s[t:]:
        return True
    else:
        return False


def invalid2(n: int) -> bool:
    s = str(n)
    l = len(s)
    for t in range(l // 2, 0, -1):
        k, r = divmod(l, t)
        if r == 0 and s == s[:t] * k:
            return True
    return False


P1 = 0
P2 = 0
for pair in puzz:
    for num in range(pair[0], pair[1] + 1):
        if invalid1(num):
            P1 += num
            continue
        if invalid2(num):
            P2 += num
            continue


print(f"Part 1: {P1}")
print(f"Part 2: {P1+P2}")
