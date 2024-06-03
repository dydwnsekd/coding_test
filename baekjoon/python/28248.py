import sys

result = 0
p = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if p > c:
    result += 500

print(result + p * 50 - c * 10)
