import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().strip().split()))
sorted(num_list)

for i in range(1, num_list[0] + 1):
    if all(num % i == 0 for num in num_list):
        print(i)
