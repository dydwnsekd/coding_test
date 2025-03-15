"""
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
"""

import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

# `2c`가 `a + b`보다 저렴하면 `2c`로 구입하는 것이 유리
if 2 * c < a + b:
    # `x`와 `y` 중 작은 개수만큼 `2c`로 먼저 구매
    min_xy = min(x, y)
    result = min_xy * 2 * c

    # 남은 피자의 개수 처리
    if x > y:
        result += min((x - y) * a, (x - y) * 2 * c)  # `a` 또는 `2c` 중 최소 비용 선택
    elif y > x:
        result += min((y - x) * b, (y - x) * 2 * c)  # `b` 또는 `2c` 중 최소 비용 선택
else:
    # 개별 가격으로 구매
    result = a * x + b * y

print(result)

