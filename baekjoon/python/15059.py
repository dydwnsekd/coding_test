import sys

result = 0

a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

for i in range(3):
    if a[i] < b[i]:
        result += b[i] - a[i]

print(result)

