import sys

s = sys.stdin.readline().strip()
result = ""
skip_count = 0

for i in range(len(s) - 1):
    if skip_count > 0:
        skip_count -= 1
        continue
    if s[i] in ['a', 'e', 'i', 'o', 'u']:
        result += s[i]
        skip_count += 2
    else:
        result += s[i]

print(result)
