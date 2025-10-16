import sys

science_score = []
society_score = []

for i in range(6):
    if i < 4:
        science_score.append(int(sys.stdin.readline().strip()))
    else:
        society_score.append(int(sys.stdin.readline().strip()))

score = sum(science_score) + sum(society_score) - min(science_score) - min(society_score)

print(score)
