import sys

result = 0
n, m = list(map(int, sys.stdin.readline().split()))

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for i in a:
    for j in b:
        if j >= i:
            result += 1

print(result)

