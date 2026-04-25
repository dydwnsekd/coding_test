import sys

result = 0

n = int(sys.stdin.readline())

a_list = list(map(int, sys.stdin.readline().strip().split()))
b_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    if a_list[i] > b_list[i]:
        result += 3
    elif a_list[i] == b_list[i]:
        result += 1

print(result)

