import sys

n = int(sys.stdin.readline())
b_list = list(map(int, sys.stdin.readline().strip().split()))
a_list = b_list[:1]

for i in range(1, n):
    a_list.append((b_list[i] * (i+1)) - sum(a_list))

print(*a_list)


