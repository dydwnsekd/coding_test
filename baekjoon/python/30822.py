import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

count = []
count_s = ['u', 'o', 's', 'p', 'c']

for c in count_s:
    count.append(s.count(c))

print(min(count))


