import sys

count = 0

n = int(sys.stdin.readline())
c1 = list(sys.stdin.readline().strip())
c2 = list(sys.stdin.readline().strip())

for i in range(n):
    if c1[i] == "C" and c2[i] == "C":
        count += 1

print(count)
