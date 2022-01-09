"""Player 1 starting position: 4
Player 2 starting position: 1"""

import functools

# part 1:
p1s = 0
p2s = 0

p1p = 4
p2p = 1

die = 0
while True:
    # player 1 rolls
    d = (die * 3 + 6) % 10
    p1p += d
    if p1p > 10:
        p1p -= 10
    p1s += p1p
    die += 3
    if p1s >= 1000:
        print(f"Part 1: {p2s * die}")
        break
    # player 2 rolls
    d = (die * 3 + 6) % 10
    p2p += d
    if p2p > 10:
        p2p -= 10
    p2s += p2p
    die += 3
    if p2s >= 1000:
        print(f"Part 1: {p1s * die}")
        break

# Part 2:
# create all possible outcomes of rolling:
rolls = list(i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4))


@functools.cache
def turn(p1pos, p1score, p2pos, p2score):
    global rolls
    w1 = w2 = 0
    # player 1 rolls
    for d in rolls:
        p1p = p1pos + d
        if p1p > 10:
            p1p -= 10
        p1s = p1score + p1p
        if p1s >= 21:
            w1 += 1
        else:
            # player 2 plays
            w2_, w1_ = turn(p2pos, p2score, p1p, p1s)
            w1 += w1_
            w2 += w2_
    return w1, w2


print(f"Part 2: {max(turn(4, 0, 1, 0))}")
