import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())
num4 = int(sys.stdin.readline())

total_second = num1 + num2 + num3 + num4

print (int(total_second/60))
print (int(total_second%60))