import sys
from collections import defaultdict

string_dict = defaultdict(int)
s = sys.stdin.readline().strip()

for i in s:
    string_dict[i] += 1

if all(v % 2 == 0 for v in string_dict.values()):
    print(0)
elif all(v % 2 == 1 for v in string_dict.values()):
    print(1)
else:
    print("0/1")

