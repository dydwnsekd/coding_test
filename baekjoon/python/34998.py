import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    expression = sys.stdin.readline().strip()

    if x == 1:
        result = int(expression[0]) + int(expression[4])
    elif x == 2:
        result = int(expression[0]) + int(expression[4]) + int(expression[8])
    else:
        result = int(expression[0]) + int(expression[4]) + int(expression[8]) + int(expression[12])

    print(result)
