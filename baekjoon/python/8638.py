import sys

result = ""

cases = int(sys.stdin.readline())
score_list = list(map(int, sys.stdin.readline().split()))

max_value = max(score_list)

for i in range(cases):
    if max_value == score_list[i]:
        result += chr(i+65)

print(result)

