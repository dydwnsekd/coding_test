import sys

n, m = list(map(int, sys.stdin.readline().split()))
k = list(map(int, sys.stdin.readline().split()))

num_list = []

for i in k:
    temp = i
    while temp <= n:
        if temp not in num_list:
            num_list.append(temp)
        temp += i

print(sum(num_list))
