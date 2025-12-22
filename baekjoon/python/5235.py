import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    num_list = list(map(int, sys.stdin.readline().strip().split()[1:]))

    even_sum = sum(v for v in num_list if v % 2 == 0)
    odd_sum = sum(v for v in num_list if v % 2 != 0)

    if even_sum < odd_sum:
        print("ODD")
    elif even_sum > odd_sum:
        print("EVEN")
    else:
        print("TIE")
