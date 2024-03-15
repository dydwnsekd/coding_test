import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
f_list = list(map(int, sys.stdin.readline().split()))

if sum(f_list) >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
