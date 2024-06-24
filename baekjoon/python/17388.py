import sys

score_list = list(map(int, sys.stdin.readline().split()))

if sum(score_list) >= 100:
    print("OK")
elif min(score_list) == score_list[0]:
    print("Soongsil")
elif min(score_list) == score_list[1]:
    print("Korea")
elif min(score_list) == score_list[2]:
    print("Hanyang")

