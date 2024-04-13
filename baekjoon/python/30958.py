import sys
from collections import defaultdict

alphabet_dict = defaultdict(int)

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for w in s:
    if w not in [" ", ",", "."]:
        alphabet_dict[w] += 1

max_count = 0

for k, v in alphabet_dict.items():
    if v > max_count:
        max_count = v

print(max_count)
