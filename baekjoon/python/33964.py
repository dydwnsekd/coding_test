import sys

x, y = map(int, sys.stdin.readline().strip().split())
x_num = ""
y_num = ""

for _ in range(x):
    x_num += "1"

for _ in range(y):
    y_num += "1"

x_num = int(x_num)
y_num = int(y_num)

print(x_num + y_num)
