import sys

max_value = 0
balance_count = 0
n, m = map(int, sys.stdin.readline().strip().split())
score_list = sorted(list(map(int, sys.stdin.readline().strip().split())))

for i in range(len(score_list) - 2):
    if max(score_list[i:i + 3]) - min(score_list[i:i + 3]) < 150:
        balance_count += 1
        if max_value < sum(score_list[i:i + 3]):
            max_value = sum(score_list[i:i + 3])

print(balance_count, max_value)

