from functools import reduce

# Part 1:
P1 = 0
L = list(line.strip().split() for line in open("06.input").readlines())
for row in range(len(L) - 1):
    L[row] = list(map(int, L[row]))
for col in range(len(L[0])):
    C = [L[row][col] for row in range(len(L) - 1)]
    Op = L[-1][col]
    match Op:
        case "*":
            P1 += reduce(lambda x, y: x * y, C)
        case "+":
            P1 += reduce(lambda x, y: x + y, C)
print(f" Part 1: {P1}")

# Part 2
P2 = 0
L = open("06.input").readlines()  # We need all caracters in the line for part 2.
T = list()
for col in range(len(L[0])):
    C = [L[row][col] for row in range(len(L) - 1)]
    if L[-1][col] == "*" or L[-1][col] == "+":
        Op = L[-1][col]
    try:
        T.append(int("".join(C)))
    except ValueError:  # This means we hit the empty column. Produce a tally here.
        match Op:
            case "*":
                P2 += reduce(lambda x, y: x * y, T)
            case "+":
                P2 += reduce(lambda x, y: x + y, T)
        T = list()
print(f" Part 2: {P2}")
