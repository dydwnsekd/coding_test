import sys

while True:
    p1, p2 = sys.stdin.readline().strip().split()
    if p1 == "#" and p2 == "#":
        break

    cases = int(sys.stdin.readline())
    p1_score = 0
    p2_score = 0

    for _ in range(cases):
        c, f = sys.stdin.readline().strip().split()
        if c == f:
            p1_score += 1
        else:
            p2_score += 1

    print(f"{p1} {p1_score} {p2} {p2_score}")
