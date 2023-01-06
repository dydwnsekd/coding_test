import sys
import math

n = int(sys.stdin.readline())

a_score = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
b_score = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
c_score = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]

t_index = [0, 3, 6]
f_index = [1, 2, 4, 5]

for i in range(n):
    total = 0
    scores = list(map(int, sys.stdin.readline().split()))
    for j in range(7):
        if j in t_index:
            total += math.floor(a_score[j] * pow(b_score[j] - scores[j], c_score[j]))
        else:
            total += math.floor(a_score[j] * pow(scores[j] - b_score[j], c_score[j]))

    print(total)
