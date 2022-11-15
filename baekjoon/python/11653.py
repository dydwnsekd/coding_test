import sys

n = int(sys.stdin.readline())

while n > 1:
    for i in range(2, 10000000):
        if n % i == 0:
            print(i)
            n = n // i
            break

