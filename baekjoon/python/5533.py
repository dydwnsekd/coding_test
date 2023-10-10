import sys

n = int(sys.stdin.readline())
score_list = [0, 0, 0]

for _ in range(n):
    temp_score = list(map(int, sys.stdin.readline().split()))

    for i in range(3):
        if temp_score.count(temp_score[i]) == 1:
            score_list[i] += temp_score[i]

for i in range(n):
    print(i)

