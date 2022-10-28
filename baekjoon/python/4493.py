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
        result = RPS(p1, p2)
        if result == 1:
            p1_score += 1
        elif result == 2:
            p2_score += 1

    if p1_score > p2_score:
        print("Player 1")
    elif p2_score > p1_score:
        print("Player 2")
    else:
        print("TIE")

