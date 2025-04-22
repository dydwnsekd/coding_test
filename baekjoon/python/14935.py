import sys

x = sys.stdin.readline().strip()
first_num = x
num_list = []

while True:
    x = str(int(x[0]) * len(x))

    if x == first_num:
        print("FA")
        break
    elif x in num_list:
        print("NFA")
        break
    else:
        num_list.append(x)

