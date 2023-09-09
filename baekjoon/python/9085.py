import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    n = int(sys.stdin.readline())
    print(sum(list(map(int, sys.stdin.readline().split()))))
