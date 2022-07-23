import sys

n, m = list(map(int, sys.stdin.readline().split()))

num_list = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    i, j = list(map(int, sys.stdin.readline().split()))

    print(sum(num_list[i-1:j]))
