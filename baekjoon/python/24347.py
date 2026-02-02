import sys
from itertools import permutations

max_value = 0
num_list = sys.stdin.readline().strip().split()

for i in permutations(num_list, 4):
    if max_value < int("".join(i)):
        max_value = int("".join(i))

print(max_value)

