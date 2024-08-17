import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, op, b, equal, answer = sys.stdin.readline().strip().split()

    if op == "+":
        if int(a) + int(b) == int(answer):
            print(f"Case {i + 1}: YES")
        else:
            print(f"Case {i + 1}: NO")
    elif op == "-":
        if int(a) - int(b) == int(answer):
            print(f"Case {i + 1}: YES")
        else:
            print(f"Case {i + 1}: NO")
