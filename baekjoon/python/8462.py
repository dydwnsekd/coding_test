# TODO
# http://www.slideshare.net/ssuser81b91b/sqrt-decomposition
# https://blog.anudeep2011.com/mos-algorithm/

import sys
from collections import defaultdict

n, t = list(map(int, sys.stdin.readline().split()))
array = list(map(int, sys.stdin.readline().split()))

for _ in range(t):
    num_dict = defaultdict(int)
    result = 0
    l, r = list(map(int, sys.stdin.readline().split()))

    for i in range(l-1, r):
        num_dict[array[i]] += 1

    for k, v in num_dict.items():
        result += k * v * v

    print(result)

