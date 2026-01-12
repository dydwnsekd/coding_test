import sys

n = int(sys.stdin.readline())
num_list = list(set(map(int, sys.stdin.readline().strip().split())))
num_list.sort()

for n in num_list:
    print(n)

