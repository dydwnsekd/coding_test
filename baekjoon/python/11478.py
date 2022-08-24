from itertools import combinations
import sys

s = sys.stdin.readline()
count = 0

for i in range(len(s)):
    print(list(combinations(s, i)))
    count += len(list(combinations(s, i)))

print(count)
