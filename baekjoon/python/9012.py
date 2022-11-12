import sys

n = int(sys.stdin.readline())

for i in range(n):
    s = sys.stdin.readline()
    left_parentheses = 0
    right_parentheses = 0

    for j in s:
        if j == "(":
            left_parentheses += 1
        elif j == ")":
            right_parentheses += 1
        if right_parentheses > left_parentheses:
            print("NO")
            break
    if left_parentheses == right_parentheses:
        print("YES")
    else:
        print("NO")
