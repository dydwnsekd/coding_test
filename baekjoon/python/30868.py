import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    quotient = n // 5
    remainder = n % 5

    for _ in range(quotient):
        print("++++", end=" ")
    for _ in range(remainder):
        print("|", end="")

    print()


