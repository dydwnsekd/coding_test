import sys

a, m = map(int, sys.stdin.readline().strip().split())

for i in range(1, 10000):
    if a * i % m == 1:
        print(i)
        break

