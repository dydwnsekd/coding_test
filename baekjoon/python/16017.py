import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())
num4 = int(sys.stdin.readline())

if (num1 in [8,9] and num4 in [8, 9]) and num2 == num3:
    print("ignore")
else:
    print("answer")

