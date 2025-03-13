import sys

result = 0

a, b, c, x, y = map(int, sys.stdin.readline().strip().split())

if a + b >= 2 * c:
    temp1 = 99999999999
    temp2 = 99999999999
    if x > y:
        result += y * 2 * c
        result += (x-y) * a
        temp1 = x * 2 * c
    elif x < y:
        result += x * 2 * c
        result += (y-x) * b
        temp2 = y * 2 * c
    else:
        result += x * 2 * c

    result = min(result, temp1, temp2)

else:
    result += a * x + b * y

print(result)

