import sys

score_list = list(map(int, sys.stdin.readline().split()))

print(56*score_list[0] + 24*score_list[1] + 14*score_list[2] + 6*score_list[3])
