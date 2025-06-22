import sys

n, h, w = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    result = ''

    rain = sys.stdin.readline().strip().split()

    if rain[0] == 'Y' or (rain[0] == 'N' and w == 0):
        h -= 1
        w += 1
        result += 'Y'
    else:
        result += 'N'
    if rain[1] == 'Y' or (rain[1] == 'N' and h == 0):
        h += 1
        w -= 1
        result += 'Y'
    else:
        result += 'N'

    print(result)

