import sys
from collections import defaultdict

sock_dict = defaultdict(int)

for _ in range(5):
    sock_dict[sys.stdin.readline().strip()] += 1

for k in sock_dict:
    if sock_dict[k] % 2 == 1:
        print(k)
