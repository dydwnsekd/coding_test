import sys
from collections import defaultdict

n = int(sys.stdin.readline())
candy_list = list(map(int, sys.stdin.readline().split()))

candy_count = defaultdict(int)

for candy in candy_list:
    candy_count[candy] += 1

for candy, count in candy_count.items():
    print(candy, count)

