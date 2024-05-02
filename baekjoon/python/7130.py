import sys

result = 0

m, h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

for _ in range(n):
    c, b = map(int, sys.stdin.readline().split())
    if c * m > b * h:
        result += c * m
    else:
        result += b * h

print(result)
