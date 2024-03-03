import sys

result = 0
n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().strip().split()))

x_list.sort()

for i in range(n-1):
    for j in range(i+1, n):
        result += abs(x_list[j] - x_list[i])

print(result * 2)
