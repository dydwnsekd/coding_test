from itertools import combinations
import sys

s = sys.stdin.readline().replace("\n", "")
partial_s = []

for i in range(1, len(s)+1):
     for j in range(len(s)-i+1):
         if s[j:i+j] not in partial_s:
             partial_s.append(s[j:i+j])

print(len(partial_s))
