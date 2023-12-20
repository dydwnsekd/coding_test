import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    score_list = list(map(int, sys.stdin.readline().split()))
    score_list = sorted(score_list)
    if score_list[-2] - score_list[1] >= 4:
        print("KIN")
    else:
        print(sum(score_list[1:-1]))
