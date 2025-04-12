import sys

kinder_list = []
n = int(sys.stdin.readline())

for i in range(n):
    kinder_list.append(sys.stdin.readline())

print(n - len(set(kinder_list)))
