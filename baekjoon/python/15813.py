import sys

result = 0

n = int(sys.stdin.readline())
name = sys.stdin.readline().strip()

for i in name:
    result += ord(i) - 64

print(result)
