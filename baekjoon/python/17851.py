# import sys
#
# count = 0
#
# team1 = sorted(map(int, sys.stdin.readline().strip().split()))
# team2 = sorted(map(int, sys.stdin.readline().strip().split()))
#
# for i in range(len(team1)):
#     if team1[i] > team2[i]:
#         count += 1
#
# print(count)

import sys

team1 = sorted(map(int, sys.stdin.readline().split()))
team2 = sorted(map(int, sys.stdin.readline().split()))

wins = sum(a > b for a, b in zip(team1, team2))
print(wins)

