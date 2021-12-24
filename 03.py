from collections import Counter

P = [line.strip() for line in open("03.txt").readlines()]

gamma = ""
D = len(P[0])
for i in range(D):
    c = Counter([l[i] for l in P])
    gamma += c.most_common()[0][0]

g = int(gamma, base=2)
e = 2 ** D - 1 - g
print(f"Part 1: {g * e}")

O = set(P)
C = set(P)

for i in range(D):
    if len(O) == 1:
        break
    t = ""
    c = Counter([l[i] for l in O]).most_common()
    if len(c) == 1:
        t = c[0][0]
    elif c[0][1] == c[1][1]:
        t = "1"
    else:
        t = c[0][0]
    O = {k for k in O if k[i] == t}

for i in range(D):
    if len(C) == 1:
        break
    t = ""
    c = Counter([l[i] for l in C]).most_common()
    if len(c) == 1:
        t = c[0][0]
    elif c[0][1] == c[1][1]:
        t = "0"
    else:
        t = c[1][0]
    C = {k for k in C if k[i] == t}

print(f"Part 2: {int(O.pop(),base=2) * int(C.pop(),base=2)}")
