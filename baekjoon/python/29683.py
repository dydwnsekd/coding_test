import sys

result = 0
n, a = list(map(int, sys.stdin.readline().split()))

a_list = list(map(int, sys.stdin.readline().split()))

for i in a_list:
    result += i // a

print(result)
