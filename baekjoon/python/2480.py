import sys

num_list = list(map(int, sys.stdin.readline().split(" ")))

set_list = set(num_list)
set_len = len(set_list)

if set_len == 1:
    print(10000 + num_list[0] * 1000)
elif set_len == 2:
    for i in num_list:
        if num_list.count(i) == 2:
            print(1000 + i * 100)
            break
else:
    print(max(num_list) * 100)
