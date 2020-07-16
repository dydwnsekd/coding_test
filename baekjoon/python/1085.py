import sys

x, y, w, h = map(int, sys.stdin.readline().split(" "))

min_list = list()

if x > abs(x-w):
    min_list.append(abs(x-w))
else:
    min_list.append(x)

if y > abs(y-h):
    min_list.append(abs(y-h))
else:
    min_list.append(y)

print (min(min_list))