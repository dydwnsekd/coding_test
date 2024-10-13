import sys

a, b, c, d = list(map(int, sys.stdin.readline().strip().split()))

print(abs((a+d) - (b+c)))
