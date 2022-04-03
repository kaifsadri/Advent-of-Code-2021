L = [line.strip() for line in open("11.txt").readlines()]


def Step():
    global G
    for dumbo in G:
        G[dumbo] += 1
    F = set(d for d in G if G[d] > 9)
    A = F.copy()
    while F:
        dumbo = F.pop()
        G[dumbo] = 0
        for coord in {(0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1)}:
            c = (dumbo[0] + coord[0], dumbo[1] + coord[1])
            if c in G and c not in A:
                G[c] += 1
                if G[c] > 9:
                    F.add(c)
                    A.add(c)
    return len(A)


# part 1: 100 steps
G = dict()
for row, line in enumerate(L):
    for col, dumbo in enumerate(line):
        G[(row, col)] = int(dumbo)
N = 0
for step in range(100):
    N += Step()
print(f"Part 1: {N}")

# part 2: Sync means Step() returns 100
for row, line in enumerate(L):
    for col, dumbo in enumerate(line):
        G[(row, col)] = int(dumbo)
Steps = 0
while True:
    Steps += 1
    if 100 == Step():
        break
print(f"Part 2: {Steps}")
