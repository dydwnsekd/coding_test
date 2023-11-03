import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    problem = sys.stdin.readline().strip().split(" ")
    a = int(problem[0])
    operator = problem[1]
    b = int(problem[2])

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a // b

    if result == int(problem[4]):
        print("correct")
    else:
        print("wrong answer")
