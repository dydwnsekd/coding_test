import sys

x, s = list(map(int, sys.stdin.readline().split()))

if x//2 < s:
    print("TAK")
else:
    print("NIE")
