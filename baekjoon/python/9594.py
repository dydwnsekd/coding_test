import sys

while True:
    n = int(sys.stdin.readline())
    temp = 1
    if n == -1:
        break

    for i in range(n+1):
        temp *= i


