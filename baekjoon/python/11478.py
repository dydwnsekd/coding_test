from itertools import combinations
import sys

s = sys.stdin.readline().strip()
result_list = []
count = 0

for i in range(len(s)+1):
    set_list = (set(combinations(s, i)))
    for j in set_list:
        temp = "".join(sorted(j))
        if temp not in result_list:
            result_list.append(temp)

print(len(result_list))
