import sys

result = 0

n = int(sys.stdin.readline())
chicken = list(map(int, sys.stdin.readline().split()))

for i in chicken:
    if i >= n:
        result += n
    else:
        result += i

print(result)
