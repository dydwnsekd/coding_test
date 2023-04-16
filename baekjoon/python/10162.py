import sys

t_list = [300, 60, 10]
c_list = []

total = int(sys.stdin.readline())

if total % 10 == 0:
    for t in t_list:
        c_list.append(total // t)
        total = total % t

    print(f"{' '.join(map(str, c_list))}")
else:
    print(-1)
