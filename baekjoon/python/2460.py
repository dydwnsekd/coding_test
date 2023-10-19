import sys

human = 0
max_human = 0

for _ in range(10):
    out_human, in_human = list(map(int, sys.stdin.readline().split()))
    human = human - out_human + in_human

    if human > max_human:
        max_human = human

print(max_human)


