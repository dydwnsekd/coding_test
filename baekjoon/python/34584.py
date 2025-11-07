import sys

x, d = map(int, sys.stdin.readline().strip().split())

if x * 2 > d:
    print("take it")
else:
    print("double it")
