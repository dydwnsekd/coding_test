import sys

num = 1
num_list = [0]

while len(num_list) < 1000:
    num_list.extend([num] * num)
    num += 1

a, b = map(int, sys.stdin.readline().strip().split())

print(sum(num_list[a:b+1]))
