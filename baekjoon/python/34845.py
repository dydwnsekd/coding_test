import sys

n, x = map(int, sys.stdin.readline().strip().split())
score_list = list(map(int, sys.stdin.readline().strip().split()))

count = 0

while True:
    if sum(score_list) / n >= x:
        break
    else:
        count += 1
        n += 1
        score_list.append(100)

print(count)
