import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    if n <= 1000000:
        print(n)
    elif n <= 5000000:
        print(int(n - n * 0.1))
    else:
        print(int(n - n * 0.2))
