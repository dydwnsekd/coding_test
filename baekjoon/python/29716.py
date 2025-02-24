import sys

result = 0
j, n = map(int, sys.stdin.readline().split())

for _ in range(n):
    s = sys.stdin.readline().strip()
    question_size = 0

    for c in s:
        if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'):
            question_size += 2
        elif ord('A') <= ord(c) <= ord('Z'):
            question_size += 4
        elif c == " ":
            question_size += 1

    if question_size <= j:
        result += 1

print(result)

