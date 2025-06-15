import sys

n = int(sys.stdin.readline())
minimum_value = 99999999999

for _ in range(n):
    t1, t2 = map(int, sys.stdin.readline().split())
    if t1 + t2 < minimum_value:
        minimum_value = t1 + t2

print(minimum_value)
