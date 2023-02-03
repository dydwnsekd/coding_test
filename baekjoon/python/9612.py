import sys
from collections import defaultdict

word_dict = defaultdict(int)
cases = int(sys.stdin.readline())

for _ in range(cases):
    word_dict[sys.stdin.readline().strip()] += 1

sorted_list = sorted(word_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

print(sorted_list[0][0], sorted_list[0][1])
