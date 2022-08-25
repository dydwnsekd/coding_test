from itertools import combinations
import sys

s = sys.stdin.readline().strip()
count = 0

for i in range(len(s)):
    print(set(combinations(s, i)))
    count += len(set(combinations(s, i)))

print(count)
