Puzz = [line.strip().split(" -> ") for line in open("05.txt").readlines()]

L = set()
for line in Puzz:
    x1, y1 = map(lambda x: int(x), line[0].split(","))
    x2, y2 = map(lambda x: int(x), line[1].split(","))
    L.add((x1, y1, x2, y2))


def step(x, y):
    if x <= y:
        return 1
    else:
        return -1


P = set()  # set of all the points that are part of H/V lines
C1 = set()  # set of intersection points on H/V lines
C2 = set()  # set of intersection points on all lines

for line in L:
    x1, y1, x2, y2 = line
    if x1 == x2 or y1 == y2:  # H/V lines
        for x in range(x1, x2 + step(x1, x2), step(x1, x2)):
            for y in range(y1, y2 + step(y1, y2), step(y1, y2)):
                if (x, y) in P:
                    C1.add((x, y))
                    C2.add((x, y))
                P.add((x, y))
    else:  # Diag lines
        for point in zip(range(x1, x2 + step(x1, x2), step(x1, x2)), range(y1, y2 + step(y1, y2), step(y1, y2))):
            if point in P:
                C2.add(point)
            P.add(point)
print(f"Part 1: {len(C1)}")
print(f"Part 2: {len(C2)}")
