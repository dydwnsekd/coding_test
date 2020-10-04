import sys

result = 0

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split(" ")))
b = list(map(int, sys.stdin.readline().split(" ")))

a.sort()
a.reverse()
b.sort()

for i in range(n):
    result += a[i] * b[i]

print(result)