import sys

result = ""
s1, s2 = sys.stdin.readline().strip().split(" ")
if len(s1) > len(s2):
    short_s = s2
    long_s = s1
else:
    short_s = s1
    long_s = s2


min_length = min(len(s1), len(s2))

for i in range(min_length):
    if i % 2 == 0:
        result += short_s[i]
    else:
        result += long_s[i]

print(result)
