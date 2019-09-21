import sys

while True:
    a, b = list(map(int, sys.stdin.readline().split(" ")))

    if a < 0 or 10 < a:
        break
    elif b < 0 or 10 < b:
        break

    print (a+b)