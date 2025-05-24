import sys
from collections import defaultdict

num_list = []
num_count_dict = defaultdict(int)

for _ in range(10):
    num = int(sys.stdin.readline())
    num_list.append(num)
    num_count_dict[num] += 1

print(sum(num_list) // 10)
print(max(num_count_dict, key=num_count_dict.get))


