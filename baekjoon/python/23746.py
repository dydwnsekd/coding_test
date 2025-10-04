import sys

n = int(sys.stdin.readline())
trans_dict = {}

for _ in range(n):
    pattern, s = sys.stdin.readline().strip().split(' ')
    trans_dict[s] = pattern

trans_str = sys.stdin.readline().strip()
s, e = map(int, sys.stdin.readline().strip().split(' '))

for k, v in trans_dict.items():
    trans_str = trans_str.replace(k, v)

print(trans_str[s-1:e])
