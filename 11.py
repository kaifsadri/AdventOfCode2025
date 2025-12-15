from functools import lru_cache

D = dict()  # device -> set of connected devices
for line in open("11.input").readlines():
    L, R = line.strip().split(": ")
    D[L] = set(R.split())


@lru_cache
def numpaths(start, finish, avoid):
    global D
    if start == finish:
        return 1
    if start in avoid or start not in D:
        return 0
    return sum(numpaths(n, finish, avoid) for n in D[start])


print(f"Part 1: {numpaths('you', 'out', ())}")
print(
    f"Part 2: {
        (
            numpaths('svr', 'fft', ('dac', 'out'))
            * numpaths('fft', 'dac', ('svr', 'out'))
            * numpaths('dac', 'out', ('fft', 'svr'))
        )
        + (
            numpaths('svr', 'dac', ('fft', 'out'))
            * numpaths('dac', 'fft', ('svr', 'out'))
            * numpaths('fft', 'out', ('dac', 'svr'))
        )
    }"
)
