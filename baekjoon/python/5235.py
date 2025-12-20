import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    odd_sum = 0
    even_sum = 0

    num_list = list(map(int, sys.stdin.readline().strip().split()[1:]))

    for num in num_list:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    if even_sum < odd_sum:
        print("ODD")
    elif even_sum > odd_sum:
        print("EVEN")
    else:
        print("TIE")
