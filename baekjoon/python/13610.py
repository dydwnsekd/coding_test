"""
import math
import sys


def overtake_time(x: int, y: int) -> int:
    if x == y:
        return -1

    v1 = 1 / x
    v2 = 1 / y
    relative_speed = abs(v1 - v2)
    time_to_overtake = 1 / relative_speed
    return math.ceil(time_to_overtake)


# 입력
x, y = map(int, sys.stdin.readline().strip().split())
print(overtake_time(x, y))
"""

# --------------------------------------------------------------------------

import sys

x, y = map(int, sys.stdin.readline().strip().split())

result = 0

x_lab = 0
y_lab = 1

while x_lab < y_lab:
    result += 1

    x_lab += 1
    y_lab += x/y

print(result)

