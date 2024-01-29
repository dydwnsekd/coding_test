import sys

a, b = list(map(int, sys.stdin.readline().split()))

result = b

for _ in range(2):
    result = (result + a) * a

print(result)
