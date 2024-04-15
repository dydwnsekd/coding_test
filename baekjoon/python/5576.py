import sys

w_list = []
k_list = []

for _ in range(10):
    w_list.append(int(sys.stdin.readline()))

for _ in range(10):
    k_list.append(int(sys.stdin.readline()))

w_list.sort()
k_list.sort()

print(sum(w_list[-3:]), sum(k_list[-3:]))
