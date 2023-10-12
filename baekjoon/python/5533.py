import sys

temp_score = []
n = int(sys.stdin.readline())

score_list = [0] * n

for _ in range(n):
    temp_score.append(list(map(int, sys.stdin.readline().split())))

pivot_score = [[row[i] for row in temp_score] for i in range(3)]

for i in range(n):
    for j in range(3):
        if pivot_score[i].count(pivot_score[i][j]) == 1:
            score_list[i] += pivot_score[i][j]

print(score_list)

