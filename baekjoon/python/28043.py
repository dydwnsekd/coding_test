"""
import sys

n, h, w = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    result = ''

    rain_h, rain_w = sys.stdin.readline().strip().split()

    if rain_h == 'Y' or (rain_h == 'N' and w == 0):
        h -= 1
        w += 1
        result += 'Y '
    else:
        result += 'N '
    if rain_w == 'Y' or (rain_w == 'N' and h == 0):
        h += 1
        w -= 1
        result += 'Y'
    else:
        result += 'N'

    print(result)
"""

import sys

n, h, w = map(int, sys.stdin.readline().split())

for _ in range(n):
    rain_h, rain_w = sys.stdin.readline().split()
    res = []

    if rain_h == 'Y' or (rain_h == 'N' and w == 0):
        h -= 1
        w += 1
        res.append('Y')
    else:
        res.append('N')

    if rain_w == 'Y' or (rain_w == 'N' and h == 0):
        h += 1
        w -= 1
        res.append('Y')
    else:
        res.append('N')

    print(' '.join(res))