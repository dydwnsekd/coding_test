"""
import sys
from collections import defaultdict

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    spell_count = defaultdict(int)
    delete_count = 0

    for c in s:
        spell_count[c] += 1

    sorted_items = sorted(spell_count.items(), key=lambda x: x[1])
    sorted_values = [v for k, v in sorted_items]

    while len(sorted_values) > 2:
        delete_count += 1
        if sorted_values[0] == 1:
            sorted_values.pop(0)
        else:
            sorted_values[0] -= 1

    print(delete_count)
"""

import sys
from collections import Counter

n = int(sys.stdin.readline().strip())

for _ in range(n):
    s = sys.stdin.readline().strip()
    freq = Counter(s)

    counts = sorted(freq.values(), reverse=True)

    delete_count = sum(counts[2:]) if len(counts) > 2 else 0

    print(delete_count)

