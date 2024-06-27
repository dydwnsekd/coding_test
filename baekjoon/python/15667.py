import sys

n = int(sys.stdin.readline())

for i in range(n):
    if i ** 2 + i + 1 == n:
        print(i)
        break
