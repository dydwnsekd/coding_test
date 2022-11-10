import sys

s = sys.stdin.readline().strip()
result = 0
pre_plate = ''

for i in range(len(s)):
    if i == 0:
        result += 10
        pre_plate = s[i]
    else:
        if pre_plate == s[i]:
            result += 5
        else:
            result += 10
            pre_plate = s[i]

print(result)
