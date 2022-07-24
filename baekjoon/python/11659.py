import sys

n, m = list(map(int, sys.stdin.readline().split()))

num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * n

for i in range(n):
    sum_list[i] = sum(num_list[0:i+1])

print(sum_list)

for _ in range(m):
    i, j = list(map(int, sys.stdin.readline().split()))

    if i == 1:
        print(sum_list[j-1])
    else:
        print(sum_list[j-1] - sum_list[i-2])
