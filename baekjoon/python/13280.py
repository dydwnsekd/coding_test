import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    score_list = list(map(int, sys.stdin.readline().strip().split()))
    score_list.sort()

    min_gap = sys.maxsize

    for i in range(n-1):
        gap = score_list[i+1] - score_list[i]
        if min_gap > gap:
            min_gap = gap

    print(min_gap)
