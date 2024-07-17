from collections import defaultdict
import sys

odd_count = 0
even_count = 0
alphabet_dict = defaultdict(int)

s = sys.stdin.readline().strip()

for i in s:
    alphabet_dict[i] += 1

for key, value in alphabet_dict.items():
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(even_count)
print(odd_count)

