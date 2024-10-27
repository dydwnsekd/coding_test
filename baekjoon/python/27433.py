import sys

result = 1
n = int(sys.stdin.readline())

for i in range(1, n+1):
    result *= i

print(result)
