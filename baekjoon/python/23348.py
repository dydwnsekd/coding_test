import sys

max_score = 0
coding_score = list(map(int, sys.stdin.readline().split()))

cases = int(sys.stdin.readline())

for _ in range(cases):
    temp = 0
    for _ in range(0, 3):
        scores = list(map(int, sys.stdin.readline().split()))
        for i in range(0, 3):
            temp += scores[i] * coding_score[i]

    if max_score < temp:
        max_score = temp

print(max_score)
