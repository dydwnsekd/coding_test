import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_rank = sorted(set(num_list))
rank_dict = {}

for i in range(len(num_rank)):
    rank_dict[num_rank[i]] = i

for num in num_list:
    print(rank_dict[num], end=" ")
