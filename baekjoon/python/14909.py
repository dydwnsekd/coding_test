import sys

result = 0
num_list = list(map(int, sys.stdin.readline().strip().split()))

for i in num_list:
    if i > 0:
        result += 1

print(result)
