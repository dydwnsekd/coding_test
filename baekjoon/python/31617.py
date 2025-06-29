import sys

count = 0

k = int(sys.stdin.readline())

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        if a[i] + k == b[j]:
            count += 1

print(count)
