L = [line.strip() for line in open("11.txt").readlines()]
G = dict()
for row, line in enumerate(L):
    for col, dumbo in enumerate(line):
        G[(row, col)] = int(dumbo)
steps = 0
tot_fl = 0
while True:
    F = set()
    A = set()
    for dumbo in G:
        G[dumbo] += 1
        if G[dumbo] > 9:
            F.add(dumbo)
    while F:
        dumbo = F.pop()
        G[dumbo] = 0
        A.add(dumbo)
        for r in range(-1, 2):
            for c in range(-1, 2):
                d = (dumbo[0] + r, dumbo[1] + c)
                if d in G and d not in A:
                    G[d] += 1
                    if G[d] > 9:
                        F.add(d)
    steps += 1
    tot_fl += len(A)
    # part 1: 100 steps
    if steps == 100:
        print(f"Part 1: {tot_fl}")
    # part 2: Sync means we had 100 flashes
    if len(A) == 100:
        print(f"Part 2: {steps}")
        break
