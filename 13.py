puz = [line.strip() for line in open("13.txt").readlines()]
P = set()
I = list()
for line in puz:
    if line == "":
        pass
    elif line[0] in "0123456789":
        P.add((int(line.split(",")[0]), int(line.split(",")[1])))
    elif line[0] == "f":
        I.append(line.split(" ")[-1])

for i, inst in enumerate(I):
    row, col = 0, 0
    l = inst.split("=")
    if l[0] == "x":
        col = int(l[1])
        for point in P.copy():
            if point[0] == col:
                P.remove(point)
            elif point[0] > col:
                P.remove(point)
                P.add((2 * col - point[0], point[1]))
    else:
        row = int(l[1])
        for point in P.copy():
            if point[1] == row:
                P.remove(point)
            elif point[1] > row:
                P.remove(point)
                P.add((point[0], 2 * row - point[1]))
    if i == 0:
        print(f"Part 1: {len(P)}")

mcol = max(point[0] for point in P)
mrow = max(point[1] for point in P)
print("Part 2:")
for row in range(mrow + 1):
    for col in range(mcol + 1):
        c = "█" if (col, row) in P else " "
        print(c, end="")
    print()
