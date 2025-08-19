import sys

difficult = []
n = int(sys.stdin.readline().strip())

for _ in range(n):
    difficult.append(int(sys.stdin.readline().strip()))

if min(difficult) == difficult[0]:
    print("ez")
elif max(difficult) == difficult[0]:
    print("hard")
else:
    print("?")
