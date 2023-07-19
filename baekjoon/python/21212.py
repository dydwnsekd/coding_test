import sys
min_value = 99999999

n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if b // a < min_value:
        min_value = b // a

print(min_value)
