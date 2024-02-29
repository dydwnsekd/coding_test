import sys

result = 0
correct_list = []

cases = int(sys.stdin.readline())

for _ in range(cases):
    correct_list.append(sys.stdin.readline().strip())

for i in range(cases):
    if correct_list[i] == sys.stdin.readline().strip():
        result += 1

print(result)
