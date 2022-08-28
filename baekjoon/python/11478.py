from itertools import combinations
import sys

s = sys.stdin.readline().replace("\n", "")
partial_s = []

for i in range(1, len(s)+1):
     for j in range(len(s)-i+1):
         partial_s.append(s[j:i+j])

print(len(set(partial_s)))
