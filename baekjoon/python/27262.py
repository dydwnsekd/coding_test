import sys

n, k, a, b = map(int, sys.stdin.readline().strip().split())

print(f"{(n + k - 2) * b} {a * (n-1)}")
