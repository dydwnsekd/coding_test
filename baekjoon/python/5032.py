import sys

e, f ,c = map(int, sys.stdin.readline().strip().split())
empty_bottle = e + f
result = 0

while empty_bottle >= c:
    temp = empty_bottle // c
    empty_bottle += temp
    empty_bottle = (empty_bottle % c) + temp

print(result)
