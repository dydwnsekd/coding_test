import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if n % 2 == 0:
    print((n // 2) + (m // 2))
    print((n // 2) - (m // 2))
else:
    print((n // 2) + 1 + (m // 2))
    print((n // 2) - (m // 2))
