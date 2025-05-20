import sys

result = ""

k = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for i in range(len(s)):
    result += chr(ord("A") + (ord(s[i]) + (3 * (i+1)) + k - ord("A")) % 26)

print(result)
