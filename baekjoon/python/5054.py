import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    answer = 0
    store_list = list(map(int, sys.stdin.readline().split()))

    print((max(store_list) - min(store_list)) * 2)
