import sys

count = 0

s = sys.stdin.readline()

for i in range(0, len(s)-1, 3):
    if s[i] != "P":
        count += 1

for i in range(1, len(s)-1, 3):
    if s[i] != "E":
        count += 1

for i in range(2, len(s)-1, 3):
    if s[i] != "R":
        count += 1

print(count)
