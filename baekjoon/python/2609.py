import sys

def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r != 0):
        r = num1 % num2
        num1, num2 = num2, r

    return (num1)


def getLCM(num1, num2):
    return int((num1 * num2) / getGCD(num1, num2))

n, m = list(map(int, sys.stdin.readline().split()))

print(getGCD(n, m))
print(getLCM(n, m))
