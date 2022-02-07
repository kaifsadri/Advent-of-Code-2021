from collections import defaultdict

H = defaultdict(lambda: 9)  # points outside the map are high points
for row, r in enumerate(list(map(lambda x: int(x), line.strip())) for line in open("09.txt").readlines()):
    for col, h in enumerate(r):
        H[(row, col)] = h

# part 1: find the low points and report the total risk value
Lows = set()
for point in H:
    adjs = [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]
    if all(H[point] < H[p] for p in adjs if p in H):
        Lows.add(point)
print(f"Part 1: {sum(1+H[point] for point in Lows)}")


# part 2:
def basin(start):
    global H
    togo = {start}
    basin = {start}
    while togo:
        point = togo.pop()
        adjs = set(
            p
            for p in [(point[0] - 1, point[1]), (point[0] + 1, point[1]), (point[0], point[1] - 1), (point[0], point[1] + 1)]
            if (H[point] < H[p] < 9 and p not in basin)
        )
        togo = togo.union(adjs)
        basin = basin.union(adjs)
    return basin


N = sorted(map(lambda lowpoint: len(basin(lowpoint)), Lows), reverse=True)
print(f"Part 2: {N[0]*N[1]*N[2]}")
