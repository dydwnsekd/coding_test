import sys

result = 0
n = int(sys.stdin.readline())
x_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(len(x_list)-1):
    for j in range(i+1, len(x_list)):
        result += abs(x_list[i] - x_list[j])

print(result * 2)
