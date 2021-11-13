import sys

def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r!=0):
        r = num1 % num2
        num1, num2 = num2, r

    return(num1)

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    print((n*m)//getGCD(n,m))