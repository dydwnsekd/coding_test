import sys

additional_points = 0
score = 0
n = int(sys.stdin.readline())

answer_list = list(map(int,sys.stdin.readline().strip().split()))
for i in answer_list:
    if i == 1:
        score += 1 + additional_points
        additional_points += 1
    else:
        additional_points = 0

print(score)
