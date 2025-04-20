import sys

x, y = map(int, sys.stdin.readline().strip().split())

result = 0

x_lab = 0
y_lab = 1

while x_lab < y_lab:
    result += 1

    x_lab += 1
    y_lab += x/y

print(result)

