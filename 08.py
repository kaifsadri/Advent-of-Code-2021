P = [line.strip().split(" | ") for line in open("08.txt").readlines()]
# part 1 is easy
N = 0
for l in P:
    for d in l[1].split():
        if len(d) in {2, 4, 3, 7}:
            N += 1
print(f"Part 1: {N}")

# Part 2:
N = 0
for l in P:
    u = l[0].split()
    # 8 is clear
    k = {8: "abcdefg"}
    n = {"abcdefg": "8"}
    # figure digits 1,4,7
    for d in u:
        if len(d) == 2:
            k[1] = "".join(sorted(d))
            n["".join(sorted(d))] = "1"
        if len(d) == 3:
            k[7] = "".join(sorted(d))
            n["".join(sorted(d))] = "7"
        if len(d) == 4:
            k[4] = "".join(sorted(d))
            n["".join(sorted(d))] = "4"
    # now figure out the 5-segment numbers
    for d in u:
        if len(d) == 5:
            if set(k[1]).issubset(set(d)):
                k[3] = "".join(sorted(d))
                n["".join(sorted(d))] = "3"
            elif len(set(k[4]).intersection(set(d))) == 3:
                k[5] = "".join(sorted(d))
                n["".join(sorted(d))] = "5"
            elif len(set(k[4]).intersection(set(d))) == 2:
                k[2] = "".join(sorted(d))
                n["".join(sorted(d))] = "2"
    # now figure out the 6-segment numbers
    for d in u:
        if len(d) == 6:
            if set(k[3]).issubset(set(d)):
                k[9] = "".join(sorted(d))
                n["".join(sorted(d))] = "9"
            elif set(k[5]).issubset(set(d)):
                k[6] = "".join(sorted(d))
                n["".join(sorted(d))] = "6"
            else:
                k[0] = "".join(sorted(d))
                n["".join(sorted(d))] = "0"
    # now figure out the 4-digit number:
    N += int("".join(n["".join(sorted(b))] for b in l[1].split()))
print(f"Part 2: {N}")
