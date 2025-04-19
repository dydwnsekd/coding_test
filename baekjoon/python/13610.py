import sys
from math import gcd

def overtake_time(x: int, y: int) -> int:
    lcm = x * y // gcd(x, y)
    return lcm // abs(x - y)

# 입력
x, y = map(int, sys.stdin.readline().strip().split())
print(overtake_time(x, y))