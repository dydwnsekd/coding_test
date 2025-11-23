"""
import sys

n,m = map(int, sys.stdin.readline().strip().split())
predict_list = []

for _ in range(n):
    predict_list.append(list(map(int, sys.stdin.readline().strip().split())))

for _ in range(m):
    count = 0
    g, x, y = map(int, sys.stdin.readline().strip().split())

    for i in range(n):
        if g >= predict_list[i][0] + predict_list[i][1] and x <= predict_list[i][0] and y <= predict_list[i][1]:
            count += 1

    print(count)
"""

import sys

n, m = map(int, sys.stdin.readline().strip().split())
pred = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

for _ in range(m):
    g, x, y = map(int, sys.stdin.readline().strip().split())
    count = 0

    g_check = g
    x_check = x
    y_check = y

    for px, py in pred:
        if px >= x_check and py >= y_check and (px + py) <= g_check:
            count += 1

    print(count)
