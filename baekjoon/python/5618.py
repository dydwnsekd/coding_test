import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, min(num_list) + 1):
    if all(num % i == 0 for num in num_list):
        print(i)

