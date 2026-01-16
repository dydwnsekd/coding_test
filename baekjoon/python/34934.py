import sys

n = int(sys.stdin.readline())

for _ in range(n):
    subject, year = sys.stdin.readline().strip().split()

    if year == '2026':
        print(subject)
        break
