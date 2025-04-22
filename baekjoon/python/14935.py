import sys

x = sys.stdin.readline().strip()
num_list = [x]

while True:
    x = str(int(x[0]) * len(x))

    if x in num_list:
        print("FA")
        break
    elif x not in num_list:
        num_list.append(x)
    elif len(x) == 1:
        print("NFA")
        break

