"""
import sys
from collections import defaultdict

n, q = map(int, sys.stdin.readline().strip().split())
name_dict = defaultdict(list)

for _ in range(n):
    name = sys.stdin.readline().strip()
    initials = name.split()[0][0] + name.split()[1][0]

    if name not in name_dict[initials]:
        name_dict[initials].append(name)

for _ in range(q):
    find_initials = sys.stdin.readline().strip()
    if len(name_dict[find_initials]) == 1:
        print(name_dict[find_initials][0])
    elif len(name_dict[find_initials]) > 1:
        print("ambiguous")
    else:
        print("nobody")
"""

import sys
from collections import defaultdict

n, q = map(int, sys.stdin.readline().strip().split())

name_dict = defaultdict(set)

for _ in range(n):
    name = input().strip()
    first, last = name.split()
    initials = first[0] + last[0]
    name_dict[initials].add(name)

for _ in range(q):
    initials = input().strip()
    names = name_dict.get(initials, set())

    if len(names) == 1:
        print(next(iter(names)))
    elif names:
        print("ambiguous")
    else:
        print("nobody")

