import sys

c = int(sys.stdin.readline())

for i in range(c):
    v,e = list(map(int, sys.stdin.readline().split(" ")))

    print (e-v+2)