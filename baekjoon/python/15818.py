import sys

result = 1
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    result *= num

print(result % m)

