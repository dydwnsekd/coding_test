import sys

count = 0
s = sys.stdin.readline().strip()

for i in range(len(s)-3):
    if s[i:i+4] == 'kick':
        count += 1

print(count)
