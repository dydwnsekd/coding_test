import sys

home_score = 0
away_score = 0

score_board = [6, 3, 2, 1, 2]

home = list(map(int, sys.stdin.readline().strip().split()))
away = list(map(int, sys.stdin.readline().strip().split()))

for i in range(5):
    home_score += score_board[i] * home[i]
    away_score += score_board[i] * away[i]

print(home_score, away_score)
