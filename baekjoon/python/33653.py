import sys

count = 0

w = sys.stdin.readline().strip()
m = int(sys.stdin.readline())

s_list = sys.stdin.readline().strip().split()

for s in s_list:
    for i in range(len(s)):
        if w == s[i:i+len(w)]:
            count += 1

print(count)

