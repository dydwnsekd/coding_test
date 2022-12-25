import sys


n = int(sys.stdin.readline())

for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))

    if b % a == 0:
        print("TAK")
    else:
        print("NIE")
