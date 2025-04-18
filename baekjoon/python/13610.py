from math import gcd

def overtake_time(x: int, y: int) -> int:
    lcm = x * y // gcd(x, y)
    return lcm // max(x, y)

# 입력 및 실행
x, y = map(int, input().split())
print(overtake_time(x, y))

