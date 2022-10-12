import sys

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    temp_num = -1
    if len(num_list) == 1:
        break
    else:
        for num in num_list[1:]:
            if num != temp_num:
                print(num, end=" ")
                temp_num = num

        print("$")
