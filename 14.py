from collections import Counter

P = [line.strip() for line in open("14.txt").readlines()]

F = dict()
for l in P[2:]:
    s = l.split(" -> ")
    F[s[0]] = s[1]

D = Counter()
T = P[0]
for i in range(len(T) - 1):
    D[T[i : i + 2]] += 1


for step in range(1, 40 + 1):
    d = Counter()
    for pair in D:
        d[pair[0] + F[pair]] += D[pair]
        d[F[pair] + pair[1]] += D[pair]
    D = d
    if step == 10:
        C = Counter()
        for k in D:
            C[k[0]] += D[k]
            C[k[1]] += D[k]
        C[T[0]] += 1
        C[T[-1]] += 1
        print(f"Part 1: {(max(C.values()) - min(C.values())) // 2}")

C = Counter()
for k in D:
    C[k[0]] += D[k]
    C[k[1]] += D[k]
C[T[0]] += 1
C[T[-1]] += 1
print(f"Part 2: {(max(C.values()) - min(C.values())) // 2}")
