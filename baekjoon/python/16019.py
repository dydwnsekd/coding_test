import sys

distance_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(5):
    for j in range(5):
        if i == j:
            print(0, end=' ')
        else:
            print(distance_list[j], end=' ')

