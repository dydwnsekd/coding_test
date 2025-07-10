"""
import sys

while True:
    s = sys.stdin.readline().strip()
    total_count = len(s)
    participant_count = 0
    y_count = 0
    n_count = 0

    if s == "#":
        break

    for c in s:
        if c == "Y":
            participant_count += 1
            y_count += 1
        elif c == "N":
            participant_count += 1
            n_count += 1
        elif c == "P":
            participant_count += 1

    if total_count // 2 < participant_count:
        if y_count > n_count:
            print("yes")
        elif y_count < n_count:
            print("no")
        elif y_count == n_count:
            print("tie")
    else:
        print("need quorum")
"""

import sys

for line in sys.stdin:
    s = line.strip()
    if s == "#":
        break

    total_count = len(s)
    y_count = s.count("Y")
    n_count = s.count("N")
    p_count = s.count("P")
    participant_count = y_count + n_count + p_count

    if participant_count > total_count // 2:
        if y_count > n_count:
            print("yes")
        elif y_count < n_count:
            print("no")
        else:
            print("tie")
    else:
        print("need quorum")


