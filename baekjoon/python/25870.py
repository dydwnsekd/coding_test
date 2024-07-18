from collections import defaultdict
import sys

odd_count = 0
even_count = 0
alphabet_dict = defaultdict(int)

s = sys.stdin.readline().strip()

for i in s:
    alphabet_dict[i] += 1

if all(i % 2 == 0 for i in alphabet_dict.values()):
    print(0)
elif all(i % 2 == 1 for i in alphabet_dict.values()):
    print(1)
else:
    print(2)

