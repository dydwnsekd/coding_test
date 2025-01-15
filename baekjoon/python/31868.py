import sys

n, k = map(int, sys.stdin.readline().strip().split())

print(k // (2 ** (n-1)))
