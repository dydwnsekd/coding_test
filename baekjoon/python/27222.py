import sys

n = int(sys.stdin.readline())
i = list(map(int, sys.stdin.readline().split()))
result = 0

for j in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if i[j] == 1 and y > x:
        result += y - x

print(result)
