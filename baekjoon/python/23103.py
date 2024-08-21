import sys

result = 0
metric_list = []
n = int(sys.stdin.readline())

for _ in range(n):
    metric = list(map(int, sys.stdin.readline().strip().split()))
    metric_list.append(metric)

for i in range(n-1):
    result += abs(metric_list[i][0] - metric_list[i+1][0]) + abs(metric_list[i][1] - metric_list[i+1][1])

print(result)
