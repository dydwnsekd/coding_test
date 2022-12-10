import sys

result = 0

n = int(sys.stdin.readline())

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()

for i in range(n):
    if s1[i] != s2[i]:
        result += 1

print(result)
