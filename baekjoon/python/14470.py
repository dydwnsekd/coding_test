import sys

result = 0

meat = 0
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())

if a < 0:
    result += (-1 * a) * c
    result += d
    result += b * e
elif a > 0:
    result += (b-a) * e

print(result)
