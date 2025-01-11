import sys

birthday_set = set()
n = int(sys.stdin.readline())

for _ in range(n):
    birthday_set.add(sys.stdin.readline().strip())

print(len(birthday_set))
