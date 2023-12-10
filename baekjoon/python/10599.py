import sys

while True:
    a, b, c, d = map(int, sys.stdin.readline().split())

    if a == b == c == d == 0:
        break

    max = abs(d - a)
    min = abs(c - b)

    print(min, max)

