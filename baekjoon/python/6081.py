import sys

n_list = []
n, q = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

for _ in range(q):
    a, b = list(map(int, sys.stdin.readline().split()))

    print(sum(n_list[a-1:b]))
