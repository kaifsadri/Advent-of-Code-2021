P = [int(a) for a in open("01.txt").readlines()]
print(f"Part 1: {sum([1 for i in range(len(P)-1) if P[i+1]>P[i]])}")
print(f"Part 2: {sum([1 for i in range(len(P)-3) if sum(P[i+1:i+4])>sum(P[i:i+3])])}")
