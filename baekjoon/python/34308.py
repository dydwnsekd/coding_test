import sys

n, k = map(int, sys.stdin.readline().strip().split())
apple_list = list(map(int, sys.stdin.readline().strip().split()))

for apple in apple_list:
    if abs(apple - 1) > abs(apple - n):
        print(n, end=" ")
    else:
        print(1, end=" ")
