import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    first_flag = True
    last_flag = True

    n, x, y = list(map(int, sys.stdin.readline().strip().split()))
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    if x == num_list[0]:
        first_flag = False
    if y == num_list[-1]:
        last_flag = False

    if all([first_flag, last_flag]):
        print("OKAY")
    elif first_flag:
        print("HARD")
    elif last_flag:
        print("EASY")
    else:
        print("BOTH")

