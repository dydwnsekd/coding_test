import sys

h, m = list(map(int, sys.stdin.readline().split()))

print((h-9) * 60 + m - 0)
