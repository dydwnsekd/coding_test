import sys

cases = int(sys.stdin.readline())
x = int(sys.stdin.readline())
result = 0

for _ in range(cases):
    p1, p2 = map(int, sys.stdin.readline().split())
    if abs(p1 - p2) <= x:
        result += max(p1, p2)
    else:
        result += int(sys.stdin.readline())

print(result)

