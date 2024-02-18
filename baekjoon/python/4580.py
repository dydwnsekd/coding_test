import sys

while True:
    result = ""
    last_sequence = 0
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    if num_list[0] == 0:
        break

    num_list = num_list[1:]

    current_num = 1
    for i in num_list:
        if i == last_sequence:
            pass
        else:
            result += (str(current_num) + " ") * (i - last_sequence)

        current_num += 1

    print(result)

