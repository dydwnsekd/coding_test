import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = list(map(int, sys.stdin.readline().split()))
    if x < y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")

