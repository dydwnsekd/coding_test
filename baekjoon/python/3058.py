import sys

t = int(sys.stdin.readline())

for _ in range(t):
    even_list = []

    num_list = list(map(int, sys.stdin.readline().strip().split()))
    for i in num_list:
        if i % 2 == 0:
            even_list.append(i)

    print(sum(even_list), min(even_list))
