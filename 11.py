from functools import cache

D = dict()  # device -> set of connected devices
for line in open("11.input").readlines():
    L, R = line.strip().split(": ")
    D[L] = set(R.split())


@cache
def numpaths(start, finish, avoid):
    global D
    if start == finish:
        return 1
    if start == avoid or start not in D:
        return 0
    return sum(numpaths(n, finish, avoid) for n in D[start])


print(f"Part 1: {numpaths('you', 'out', '')}")
print(
    f"Part 2: {
        numpaths('svr', 'fft', 'dac') * numpaths('fft', 'dac', 'out') * numpaths('dac', 'out', 'fft')
        + numpaths('svr', 'dac', 'fft') * numpaths('dac', 'fft', 'out') * numpaths('fft', 'out', 'dac')
    }"
)
