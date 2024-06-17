import sys


def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r!=0):
        r = num1 % num2
        num1, num2 = num2, r

    return(num1)


n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(getGCD(a, b))

