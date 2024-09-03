import sys

w_count = 0

for _ in range(6):
    r = sys.stdin.readline().strip()

    if r == "W":
        w_count += 1

if w_count >= 5:
    print(1)
elif w_count >= 3:
    print(2)
elif w_count >= 1:
    print(3)
else:
    print(-1)
