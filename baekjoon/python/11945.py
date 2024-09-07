import sys

n, bread_len = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    print(sys.stdin.readline().strip()[::-1])
