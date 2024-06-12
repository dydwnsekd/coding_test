import sys

n = int(sys.stdin.readline())
flag = True

for _ in range(3):
    num_list = map(int, sys.stdin.readline().strip().split())

    if 7 not in num_list:
        flag = False

if flag:
    print("777")
else:
    print("0")


