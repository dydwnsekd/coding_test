import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    temp_list = list(map(int, sys.stdin.readline().strip().split()))
    k = temp_list[0]
    num_list = temp_list[1:]

    pibonacci_flag = True

    for i in range(k-2):
        if num_list[i] + num_list[i+1] != num_list[i+2]:
            pibonacci_flag = False
            break

    if pibonacci_flag:
        print("YES")
    else:
        print("NO")

