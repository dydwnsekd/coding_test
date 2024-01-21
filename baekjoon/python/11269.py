import sys

count = 0

s = sys.stdin.readline()

for i in range(0, len(s)-1):
    if i % 3 == 0 and s[i] != "P":
        count += 1

    elif i % 3 == 1 and s[i] != "E":
        count += 1

    elif i % 3 == 2 and s[i] != "R":
        count += 1

print(count)
