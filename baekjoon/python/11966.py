import sys

square_list = []
for i in range(31):
    square_list.append(2 ** i)

n = int(sys.stdin.readline())

if n in square_list:
    print(1)
else:
    print(0)
