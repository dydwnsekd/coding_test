import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

result = ""

for c in t:
    if c not in s:
        result += c

print(result)
