import sys

n, m = list(map(int, sys.stdin.readline().split()))

num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * n
sum_list[0] = num_list[0]

for i in range(1, n):
    sum_list[i] = sum_list[i-1] + num_list[i]

for _ in range(m):
    i, j = list(map(int, sys.stdin.readline().split()))

    if i == 1:
        print(sum_list[j-1])
    else:
        print(sum_list[j-1] - sum_list[i-2])
