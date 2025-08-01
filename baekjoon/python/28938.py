"""
import sys

n = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

count_plus_1 = sequence_list.count(1)
count_minus_1 = sequence_list.count(-1)

if count_plus_1 == count_minus_1:
    print("Stay")
elif count_plus_1 > count_minus_1:
    print("Right")
else:
    print("Left")
"""

import sys

n = int(sys.stdin.readline())
sequence_list = list(map(int, sys.stdin.readline().split()))

if sum(sequence_list) == 0:
    print("Stay")
elif sum(sequence_list) > 0:
    print("Right")
else:
    print("Left")

