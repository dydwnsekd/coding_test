import sys

try:
    x, y = map(int, sys.stdin.readline().strip().split())
    print(x - y)
except Exception as e:
    print("NaN")

