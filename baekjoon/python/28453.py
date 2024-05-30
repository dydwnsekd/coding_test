import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().strip().split()))

for i in m:
    if i == 300:
        print(1, end=" ")
    elif i >= 275:
        print(2, end=" ")
    elif i >= 250:
        print(3, end=" ")
    else:
        print(4, end=" ")
