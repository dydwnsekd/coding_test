import sys
def getGCD(num1, num2):
    r = -1
    if num1 < num2:
        num1, num2 = num2, num1

    while r != 0:
        r = num1 % num2
        num1, num2 = num2, r

    return num1

cases = int(sys.stdin.readline())
for _ in range(cases):
    result = 0
    num_list = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(num_list)-1):
        result += getGCD(num_list[i], num_list[i+1])

    print(result)
