"""
import sys

n = sys.stdin.readline().strip()
champernowne_flag = True
find_num = '1'
find_index = 0

while True:
    n_num = n[find_index:find_index+len(find_num)]
    if n_num == find_num:
        find_index += len(find_num)
        find_num = str(int(find_num) + 1)
    elif find_index == len(n):
        break
    else:
        champernowne_flag = False
        break

if champernowne_flag:
    print(int(find_num) - 1)
else:
    print(-1)
"""

import sys

sequence = sys.stdin.readline().strip()
target = '1'
index = 0

while index < len(sequence):
    current = sequence[index:index + len(target)]
    if current != target:
        print(-1)
        break
    index += len(target)
    target = str(int(target) + 1)
else:
    print(int(target) - 1)
