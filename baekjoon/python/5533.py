import sys

temp_score = []
n = int(sys.stdin.readline())

score_list = [0] * n

for _ in range(n):
    temp_score.append(list(map(int, sys.stdin.readline().split())))

pivot_score = [[row[i] for row in temp_score] for i in range(3)]

for i in range(n):
    for j in range(3):
        if pivot_score[j].count(pivot_score[j][i]) == 1:
            score_list[i] += pivot_score[j][i]

for s in score_list:
    print(s)
