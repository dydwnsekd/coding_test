import sys
import re

atomic_weight = {"C": 12.01, "H": 1.008, "O": 16.00, "N": 14.01}
atomic_regex = re.compile("[CHON]")

n = int(sys.stdin.readline())

for i in range(n):
    atomic = sys.stdin.readline().strip()
    atomic_count = {"C": 0, "H": 0, "O": 0, "N": 0}

    for j in range(len(atomic)-1):
        if atomic_regex.match(atomic[j]):
            if atomic_regex.match(atomic[j+1]):
                atomic_count[atomic[j]] += 1
            else:
                atomic_count[atomic[j]] += int(atomic[j+1])

    print(atomic_count)
