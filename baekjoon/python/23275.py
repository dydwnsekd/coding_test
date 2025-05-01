import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = sys.stdin.readline().strip().split()
    y = sys.stdin.readline().strip().split()

    x_y = []

    for xi in x:
        if xi not in y:
            x_y.append(xi)

print("".join(x_y))
