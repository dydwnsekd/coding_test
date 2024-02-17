import sys
from itertools import permutations

num_list = []
a, b, c = map(int, sys.stdin.readline().strip().split())
x = int(sys.stdin.readline())
permutation_list = permutations([a, b, c], 3)

for i in permutation_list:
    num_list.append(int("".join(map(str, i))))

num_list.sort()

print(num_list.index(x) + 1)

