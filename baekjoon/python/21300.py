import sys

result = 0
bottle_list = list(map(int, sys.stdin.readline().split()))

for i in bottle_list:
    result += i*5

print(result)
