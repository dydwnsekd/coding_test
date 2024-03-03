import sys

result = 0
n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().strip().split()))

x_list.sort()

prefix_sum = [0] * n

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + (x_list[i] - x_list[i - 1]) * i

result = sum(prefix_sum)

print(result * 2)
