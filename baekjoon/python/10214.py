import sys

t = int(sys.stdin.readline())

for _ in range(t):
    yonsei_score = 0
    korea_score = 0

    for _ in range(9):
        scores = list(map(int, sys.stdin.readline().strip().split()))

        yonsei_score += scores[0]
        korea_score += scores[1]

    if yonsei_score > korea_score:
        print("Yonsei")
    elif yonsei_score < korea_score:
        print("Korea")
    else:
        print("Draw")


