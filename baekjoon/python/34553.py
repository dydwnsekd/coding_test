import sys

score = 0
result = 0
s = sys.stdin.readline().strip()
current_c = 'z'

for c in s:
    if ord(current_c) < ord(c):
        score += 1
        current_c = c
        result += score
    else:
        score = 1
        current_c = c
        result += score

print(result)
