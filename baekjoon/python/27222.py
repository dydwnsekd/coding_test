import sys

n = int(sys.stdin.readline())
i = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if i == 1 and y > x:
        result += y - x

print(result)
