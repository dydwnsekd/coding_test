import sys

result = 0
n = int(sys.stdin.readline())

for _ in range(n):
    h, b, k = map(int, sys.stdin.readline().split())
    if b > h:
        result += (b-h) * k

print(result)
