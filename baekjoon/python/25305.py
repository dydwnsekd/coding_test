import sys

n, k = list(map(int, sys.stdin.readline().split()))
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort(reverse=True)

print(num_list[k-1])
