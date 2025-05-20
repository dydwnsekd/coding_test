import sys

result = ""

k = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for c in s:
    result += chr(ord("A") + (ord(c) + k) % 26)

print(result)
