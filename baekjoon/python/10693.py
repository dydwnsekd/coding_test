import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())

    print("Case {}: {}".format(i+1, m-(n-1)))
