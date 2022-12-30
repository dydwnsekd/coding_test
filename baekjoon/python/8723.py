import sys

edge_list = list(map(int, sys.stdin.readline().split()))
edge_list.sort()

if pow(edge_list[2], 2) == pow(edge_list[0], 2) + pow(edge_list[1], 2):
    print(1)
elif edge_list[0] == edge_list[2]:
    print(2)
else:
    print(0)
