import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip().split()

result = ""

for c in a:
    if c in b:
        result += c.lower()
    else:
        result += c

print(result)

