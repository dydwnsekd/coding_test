"""
import sys
from collections import defaultdict

y = sys.stdin.readline().strip()

while True:
    y = str(int(y) + 1)

    num_dict = defaultdict(int)
    for c in y:
        num_dict[c] += 1

    if len(num_dict) == len(y):
        break

print(y)
"""

import sys

year = sys.stdin.readline().strip()

while True:
    year = str(int(year) + 1)
    if len(set(year)) == len(year):
        break

print(year)

