P = [line for line in open("10.txt").readlines()]

syntaxpoints = {")": 3, "]": 57, "}": 1197, ">": 25137}
completionpoints = {")": 1, "]": 2, "}": 3, ">": 4}
openers = {"(": ")", "<": ">", "{": "}", "[": "]"}

part1 = 0
part2 = list()
for l in P:
    expected = list()
    for c in l:
        if c == "\n":
            score = 0
            while expected:
                score = score * 5 + completionpoints[expected.pop()]
            part2.append(score)
        elif c in openers:
            expected.append(openers[c])
        else:
            if expected.pop() != c:
                part1 += syntaxpoints[c]
                break

print(f"Part 1: {part1}")
print(f"Part 2: {sorted(part2)[len(part2)//2]}")
