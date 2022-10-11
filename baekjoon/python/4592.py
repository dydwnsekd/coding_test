import sys

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if len(num_list) == 1:
        break
    else:
        set_list = set(num_list[1:])
        for num in set_list:
            print(num, end=" ")
        print("$")
