import sys

n, k = map(int, sys.stdin.readline().strip().split())
apple_list = list(map(int, sys.stdin.readline().strip().split()))

for apple in apple_list:
    if apple >= n / 2:
        print(n, end=" ")
    else:
        print(1, end=" ")
