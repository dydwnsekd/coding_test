import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.sort()

    print(num_list[-3])
