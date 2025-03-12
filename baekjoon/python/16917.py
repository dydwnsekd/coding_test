import sys

result = 0

a, b, c, x, y = map(int, sys.stdin.readline().strip().split())

if a + b >= 2 * c:
    if x > y:
        result += y * 2 * c
        result += (x-y) * a
    elif x < y:
        result += x * 2 * c
        result += (y-x) * b
else:
    result += a * x + b * y

print(result)

