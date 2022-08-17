import sys

while True:
    n, m = list(map(int, sys.stdin.readline().split()))
    if n == 0 and m == 0:
        break
    else:
        if m % n == 0:
            print("factor")
        elif n % m == 0:
            print("multiple")
        else:
            print("neither")
