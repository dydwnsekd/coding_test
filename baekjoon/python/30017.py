import sys

a, b = map(int, sys.stdin.readline().strip().split())

max_size = -1

if a - 1 <= b:
    max_size = 2 * a - 1
elif a + 1 >= b:
    max_size = 2 * b + 1

print(max_size)
