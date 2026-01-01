import sys

result = 0
n, m = map(int, sys.stdin.readline().strip().split())

a_list = list(map(int, sys.stdin.readline().strip().split()))
b_list = list(map(int, sys.stdin.readline().strip().split()))

for a in a_list:
    for b in b_list:
        result += (a+b) * max(a, b)

print(result)
