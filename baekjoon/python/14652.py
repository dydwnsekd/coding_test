import sys

n, m, k = map(int, sys.stdin.readline().strip().split())

print(k//m, k%m)
