import sys

n = int(sys.stdin.readline())
t_list = []
d_list = []
max_speed = -1

for _ in range(n):
    t, d = map(int, sys.stdin.readline().split())
    t_list.append(t)
    d_list.append(d)

for i in range(1, n):
    if max_speed < (d_list[i] - d_list[i-1]) // (t_list[i] - t_list[i-1]):
        max_speed = (d_list[i] - d_list[i-1]) // (t_list[i] - t_list[i-1])

print(max_speed)

