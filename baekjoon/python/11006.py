import sys

c = int(sys.stdin.readline())

for i in range(c):
    n,m = list(map(int, sys.stdin.readline().split(" ")))

    cut_leg = m*2-n
    print("%d %d" % (cut_leg, m-cut_leg))