import sys

count = 0
answer = int(sys.stdin.readline())
quiz = list(map(int, sys.stdin.readline().split()))

for i in quiz:
    if i == answer:
        count += 1

print(count)

