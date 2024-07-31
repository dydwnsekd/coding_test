import sys

n, a, b = map(int, sys.stdin.readline().strip().split())

if n > b:
    print("Bus")
else:
    if a == b:
        print("Anything")
    elif a > b:
        print("Subway")
    else:
        print("Bus")


