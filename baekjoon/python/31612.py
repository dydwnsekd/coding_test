import sys

result = 0
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for i in s:
    if i == "o":
        result += 1
    else:
        result += 2

print(result)

