P = list(map(lambda x: int(x), open("06.txt").readline().strip().split(",")))

# There are not a lot of crabs, fo brue-force works for both parts
F1 = F2 = 1e12  # some large number
for i in range(min(P), max(P) + 1):  # alignment position is somewhere between the crabs
    f1 = f2 = 0
    for c in P:
        f1 += abs(c - i)
        f2 += abs(c - i) * (abs(c - i) + 1) / 2
    F1 = min(F1, f1)
    F2 = min(F2, f2)
print(f"Part 1: {F1}")
print(f"Part 2: {F2:.0f}")
