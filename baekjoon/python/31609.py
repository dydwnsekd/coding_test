import sys

n = int(sys.stdin.readline())
num = sys.stdin.readline().strip()
num_list = list(set([int(n) for n in num]))
num_list.sort()

for n in num_list:
    print(n)

