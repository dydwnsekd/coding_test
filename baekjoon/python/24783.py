import sys

def operator_possible(a, b, c):
    if b > a:
        a, b = b, a

    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    else:
        return False


cases = int(sys.stdin.readline())

for _ in range(cases):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if operator_possible(a, b, c):
        print("Possible")
    else:
        print("Impossible")

