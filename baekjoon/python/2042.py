import sys

num_list = []
n, m, k = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    num_list.append(int(input))

for _ in range(m+k):
    a, b, c = list(map(int, sys.stdin.readline().split()))

    if a == 1:
        num_list[b] = c
    elif a == 2:
        print(sum(num_list[b:c+1]))
