import sys
from collections import Counter

cases = int(sys.stdin.readline())
upper_str = ""
lower_str = ""

for _ in range(cases):
    s = sys.stdin.readline().strip().replace(" ", "")
    for i in s:
        if ord("a") <= ord(i) <= ord("z"):
            lower_str += i
        else:
            upper_str += i

count_lower_str = Counter(lower_str)
count_upper_str = Counter(upper_str)
sorted_lower_dict = sorted(count_lower_str.items())
sorted_upper_dict = sorted(count_upper_str.items())

for i in sorted_lower_dict:
    print(i[0], i[1])

for i in sorted_upper_dict:
    print(i[0], i[1])

