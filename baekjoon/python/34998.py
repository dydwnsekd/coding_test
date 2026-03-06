import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    expression = sys.stdin.readline().strip()

    if x == 1:
        if expression[0] == "!" or expression[4] == "!":
            result = -1
        else:
            result = int(expression[0]) + int(expression[4])
    elif x == 2:
        if expression[0] == "!" or expression[4] == "!" or expression[8] == "!":
            result = -1
        else:
            result = int(expression[0]) + int(expression[4]) + int(expression[8])
    else:
        if expression[0] == "!" or expression[4] == "!" or expression[8] == "!" or expression[12] == "!":
            result = -1
        else:
            result = int(expression[0]) + int(expression[4]) + int(expression[8]) + int(expression[12])

    if result >= 10 or result == -1:
        print("!")
    else:
        print(result)
