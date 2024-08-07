import sys

flag = False

n = int(sys.stdin.readline())
x, s = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    v, p = map(int, sys.stdin.readline().strip().split())

    if x >= v and p > s:
        flag = True

if flag:
    print("YES")
else:
    print("NO")
