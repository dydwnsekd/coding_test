import sys

count = 0
x, y = list(map(int, sys.stdin.readline().split()))

if len(x) == len(y):
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1

