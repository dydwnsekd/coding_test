import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
find_num = int(sys.stdin.readline())

print(num_list.count(find_num))
