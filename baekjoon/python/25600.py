import sys

cases = int(sys.stdin.readline())
max_value = 0

for _ in range(cases):
    a, d, g = map(int, sys.stdin.readline().split())

    if a == d+g:
        temp = 2 * a * (d+g)
    else:
        temp = a * (d + g)

    if temp > max_value:
        max_value = temp

print(max_value)
