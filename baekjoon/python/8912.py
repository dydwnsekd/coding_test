import sys

cases = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for _ in range(cases):
    sales_list = list(map(int, sys.stdin.readline().split()))
    count = 0

    for i in range(1, len(sales_list)):
        for j in range(0, i):
            if sales_list[i] >= sales_list[j]:
                count += 1

    print(count)
