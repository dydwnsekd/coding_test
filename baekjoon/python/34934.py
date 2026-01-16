"""
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    subject, year = sys.stdin.readline().strip().split()

    if year == '2026':
        print(subject)
        break
"""

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
subject_dict = defaultdict(list)

for _ in range(n):
    subject, year = sys.stdin.readline().strip().split()
    subject_dict[year].append(subject)

print(subject_dict['2026'][0])


