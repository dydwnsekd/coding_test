import sys

count = 0

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
reverse_s = s[::-1]

for i in range(n):
    if s[i] != reverse_s[i]:
        count += 1

print(count//2)
