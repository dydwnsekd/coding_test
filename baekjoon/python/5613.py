import sys

result = 0
operator = ""

is_first = True
sequence = 0

while True:
    s = sys.stdin.readline().strip()

    if sequence == 0:
        result = int(s)
    elif sequence % 2 == 1:
        operator = s
    elif sequence % 2 == 0:
        if operator == "+":
            result += int(s)
        elif operator == "-":
            result -= int(s)
        elif operator == "*":
            result *= int(s)
        elif operator == "/":
            result //= int(s)
    if s == "=":
        print(result)
        break

    sequence += 1

