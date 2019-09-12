import sys

x = int(sys.stdin.readline())
y_1 = int(sys.stdin.readline())
y_2 = int(sys.stdin.readline())
y_3 = int(sys.stdin.readline())
p = int(sys.stdin.readline())

x_value = x * p
if y_2 >= p:
    y_value = y_1
else:
    y_value = y_1 + ((p-y_2) * y_3)

if x_value < y_value:
    print(x_value)
else:
    print(y_value)