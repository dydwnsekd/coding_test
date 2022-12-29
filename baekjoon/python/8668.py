import sys

x, s = list(map(int, sys.stdin.readline().split()))

while True:
    if x >= s:
        print("TAK")
        break
    else:
        s -= x
        x /= 2

        if s > x:
            print("NIE")
            break
