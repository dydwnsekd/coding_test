import sys

num1, op, num2, equals, result = sys.stdin.readline().strip().split()

if int(num1) + int(num2) == int(result):
    print("YES")
else:
    print("NO")

