import sys

result = ""
prev_s = ""
s = sys.stdin.readline().strip()

for i in s:
    if i != prev_s:
        result += i
        prev_s = i

print(result)
