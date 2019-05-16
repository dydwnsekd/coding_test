import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())

result = [0 for i in range(10)]

num = num1 * num2 * num3
num = str(num)

for s in num:
    s = int(s)
    result[s] = result[s] + 1

for i in result:
    print (i)

