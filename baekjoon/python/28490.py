import sys

max_value = 0
n = int(sys.stdin.readline())

for _ in range(n):
    w, h = map(int, sys.stdin.readline().strip().split())
    if max_value < w * h:
        max_value = w * h

print(max_value)
