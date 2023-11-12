import sys

s, t, d = list(map(int, sys.stdin.readline().split()))

print((d//(s*2)) * t)
