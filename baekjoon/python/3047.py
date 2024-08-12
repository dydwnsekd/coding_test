import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))
sort_str = sys.stdin.readline().strip()

num_list.sort()

for s in sort_str:
    if s == "A":
        print(num_list[0], end=" ")
    elif s == "B":
        print(num_list[1], end=" ")
    elif s == "C":
        print(num_list[2], end=" ")

