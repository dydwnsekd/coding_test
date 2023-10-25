import sys

alphabet_count = [0] * 26
s = sys.stdin.readline().strip()

for i in s:
    alphabet_count[ord(i)-97] += 1

print(*alphabet_count)
