P = [line.split() for line in open("02.txt").readlines()]
h, d = 0, 0
for line in P:
    if line[0] == "forward":
        h += int(line[1])
    elif line[0] == "up":
        d -= int(line[1])
    elif line[0] == "down":
        d += int(line[1])
print(f"Part 1: {h * d}")

h, d, a = 0, 0, 0
for line in P:
    if line[0] == "forward":
        h += int(line[1])
        d += int(line[1]) * a
    elif line[0] == "up":
        a -= int(line[1])
    elif line[0] == "down":
        a += int(line[1])
print(f"Part 2: {h * d}")
