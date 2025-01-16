import sys

alphabet_dict = {}
index = 0
result = ""

for i in range(ord('A'), ord('Z')+1):
    alphabet_dict[chr(i)] = i - ord('A') + 1

s = sys.stdin.readline().strip()

while index < len(s):
    result += s[index]

    index += alphabet_dict[s[index]]

print(result)
