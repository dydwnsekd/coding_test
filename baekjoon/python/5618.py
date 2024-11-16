import sys

def getGCD(num1, num2):
    r = -1
    if num1 < num2: num1, num2 = num2, num1

    while (r!=0):
        r = num1 % num2
        num1, num2 = num2, r

    return(num1)

def get_divisor(num):

    divisor_list = []
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 2]
    elif num == 3:
        return [1, 3]

    for i in range(1, num//2 + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num // i)

    divisor_list = list(set(divisor_list))
    divisor_list.sort()
    return divisor_list

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))

gcd = getGCD(num_list[0], num_list[1])

if n == 3:
    gcd = getGCD(gcd, num_list[2])

divisor = get_divisor(gcd)
for i in divisor:
    print(i)


