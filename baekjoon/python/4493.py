import sys


def RPS(p1, p2):
    if p1 == p2:
        return 0
    elif p1 == "R":
        if p2 == "P":
            return 2
        elif p2 == "S":
            return 1
    elif p1 == "P":
        if p2 == "R":
            return 1
        elif p2 == "S":
            return 2
    elif p1 == "S":
        if p2 == "R":
            return 2
        elif p2 == "P":
            return 1


n = int(sys.stdin.readline())

for _ in range(n):
    case = int(sys.stdin.readline())
    p1_score = 0
    p2_score = 0

    for _ in range(case):
        p1, p2 = list(sys.stdin.readline().split())
        if p1 == p2:
            pass

