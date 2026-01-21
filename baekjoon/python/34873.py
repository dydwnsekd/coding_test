import sys
from collections import defaultdict

n = int(sys.stdin.readline())
candy_list = list(map(int, sys.stdin.readline().split()))
success_count = 0

candy_count = defaultdict(int)

for candy in candy_list:
    candy_count[candy] += 1

for candy, count in candy_count.items():
    if count > 1:
        success_count += 1
    elif count == 1:
        success_count += 0.5

if success_count >= n:
    print('Yes')
else:
    print('No')

