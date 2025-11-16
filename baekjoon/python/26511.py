import sys
from collections import defaultdict

from redis import UsernamePasswordCredentialProvider

n = int(sys.stdin.readline())

for _ in range(n):
    s = sys.stdin.readline().strip()
    spell_count = defaultdict(int)
    delete_count = 0

    for c in s:
        spell_count[c] += 1
        sorted_values = [v for k, v in spell_count]

    while len(sorted_values) <= 2:
        delete_count += 1
        if sorted_values[0] == 1:
            sorted_values.pop(0)
        else:
            sorted_values[0] -= 1

    print(delete_count)


