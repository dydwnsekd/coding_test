import sys

n = int(sys.stdin.readline())

for _ in range(n):
    case = int(sys.stdin.readline())
    p1_score = 0
    p2_score = 0

    for _ in range(case):
        p1, p2 = list(sys.stdin.readline().split())
        if p1 == p2:
            pass

