import sys

n, x = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if x > num_list[i]:
        print (num_list[i], end=' ')