import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

if 2 * c < a + b:
    min_xy = min(x, y)
    result = min_xy * 2 * c

    if x > y:
        result += min((x - y) * a, (x - y) * 2 * c)
    elif y > x:
        result += min((y - x) * b, (y - x) * 2 * c)
else:
    result = a * x + b * y

print(result)

