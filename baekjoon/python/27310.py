import sys

result = 0
s = sys.stdin.readline().strip()

for i in s:
    if i == ":":
        result += 1
    elif i == "_":
        result += 5

print((len(s) + result))

