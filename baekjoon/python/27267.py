import sys

a, b, c, d = map(int, sys.stdin.readline().split())

if a * b > c * d:
    print("M")
elif a * b == c * d:
    print("E")
else:
    print("P")
