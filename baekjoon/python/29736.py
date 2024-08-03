import sys

count = 0
a, b = map(int, sys.stdin.readline().strip().split())
k, x = map(int, sys.stdin.readline().strip().split())

for i in range(a, b+1):
    if k - x <= i <= k + x:
        count += 1

if count == 0:
    print("IMPOSSIBLE")
else:
    print(count)
