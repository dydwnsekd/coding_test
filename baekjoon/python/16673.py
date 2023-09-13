import sys

result = 0
c, k, p = list(map(int, sys.stdin.readline().split()))

for i in range(1, c+1):
    result += i*k + i*i*p

print(result)
