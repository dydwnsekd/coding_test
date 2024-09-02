import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().strip().split()))

    print(min(num_list), max(num_list))
