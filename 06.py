A = [0] * 9  # A contains an array of the number of lantern fish at each age, ranging from 0 to 8.
for fish in map(lambda x: int(x), open("06.txt").readline().strip().split(",")):  # Age-bucket the fish
    A[fish] += 1

for day in range(80):
    A[7] += A[0]  # this simulates the 0's becoming 6
    A = A[1:] + [A[0]]  # this simulates the 0's spawning 8's
print(f"Part 1: {sum(A)}")
for day in range(80, 256):
    A[7] += A[0]
    A = A[1:] + [A[0]]
print(f"Part 2: {sum(A)}")
