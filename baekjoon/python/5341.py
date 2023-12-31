import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    else:
        print(sum([i for i in range(n, 0, -1)]))
