import sys

handle_list = []
n, l = list(map(int, sys.stdin.readline().split()))

for _ in range(n):
    handle_list.append(sys.stdin.readline().strip())

handle_list.sort()
print(handle_list[l-1])
