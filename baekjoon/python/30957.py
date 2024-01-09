import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
B_count = 0
S_count = 0
A_count = 0
result = ""

for i in s:
    if i == "B":
        B_count += 1
    elif i == "S":
        S_count += 1
    elif i == "A":
        A_count += 1

max_count = max([B_count, S_count, A_count])
if max_count == B_count == S_count == A_count:
    result += "SCU"
else:
    if B_count == max_count:
        result += "B"
    if S_count == max_count:
        result += "S"
    if A_count == max_count:
        result += "A"

print(result)

