import sys

def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r!=0):
        r = num1 % num2
        num1, num2 = num2, r

    return(num1)

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))

gcd = getGCD(num_list[0], num_list[1])

if n == 3:
    gcd = getGCD(gcd, num_list[2])

for i in range(1, gcd+1):
    if gcd % i == 0:
        print(i)

