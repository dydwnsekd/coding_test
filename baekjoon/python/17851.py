import sys

count = 0

team1 = sorted(map(int, sys.stdin.readline().strip().split()))
team2 = sorted(map(int, sys.stdin.readline().strip().split()))

for i in range(len(team1)):
    if team1[i] > team2[i]:
        count += 1

print(count)
