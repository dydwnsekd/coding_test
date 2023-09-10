import sys

n, m = list(map(int, sys.stdin.readline().split()))
k = list(map(int, sys.stdin.readline().split()))

num_list = []

for i in k:
    temp = i
    while temp < n+1:
        if temp not in num_list:
            num_list.append(temp)
        temp += temp

print(num_list)
print(sum(num_list))
