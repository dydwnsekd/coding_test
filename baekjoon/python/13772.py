import sys

one_hole = ["A", "D", "O", "P", "Q", "R"]
two_hole = ["B"]

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline().strip()

    hole_count = 0

    for c in s:
        if c in one_hole:
            hole_count += 1
        elif c in two_hole:
            hole_count += 2

    print(hole_count)


