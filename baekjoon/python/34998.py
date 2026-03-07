"""
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
"""

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    expression = sys.stdin.readline()

    operand_cnt = x + 1
    tokens = expression.split()
    nums = tokens[0::2]

    if len(nums) < operand_cnt or any(v == "!" for v in nums[:operand_cnt]):
        result = -1
    else:
        result = sum(int(v) for v in nums[:operand_cnt])

    if result == -1 or result >= 10:
        print("!")
    else:
        print(result)

