import sys
from collections import Counter

cases = int(sys.stdin.readline())
all_str = ""

for _ in range(cases):
    all_str += sys.stdin.readline().strip().replace(" ", "")

count_str = Counter(all_str)
print(count_str)

