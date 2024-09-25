import sys

count = 0
n, m = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    goal_list = list(map(int, sys.stdin.readline().strip().split()))

    if all(goal > 0 for goal in goal_list):
        count += 1

print(count)

