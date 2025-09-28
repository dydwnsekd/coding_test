import sys

n = int(sys.stdin.readline())
name_list = []

for _ in range(n):
    name = sys.stdin.readline().strip()
    if len(name) == 3:
        name_list.append(name)

print(sorted(name_list)[0])
