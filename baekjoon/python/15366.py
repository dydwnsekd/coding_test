import sys

n = int(sys.stdin.readline())

x_list = list(map(int, sys.stdin.readline().split()))
y_list = list(map(int, sys.stdin.readline().split()))

x_list.sort()
y_list.sort()

flag = True

for i in range(n):
    if x_list[i] > y_list[i]:
        flag = False
        break

if flag:
    print("DA")
else:
    print("NE")

