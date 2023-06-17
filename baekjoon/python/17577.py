import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    max_sum = 0

    for _ in range(m):
        score_list = list(map(int, sys.stdin.readline().split()))
        if max_sum < sum(score_list):
            max_sum = sum(score_list)

    print(max_sum)

