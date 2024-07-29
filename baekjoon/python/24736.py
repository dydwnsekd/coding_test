import sys

score_board = [6, 3, 2, 1, 2]

home = list(map(int, sys.stdin.readline().strip().split()))
away = list(map(int, sys.stdin.readline().strip().split()))

home_score = sum(s * h for s, h in zip(score_board, home))
away_score = sum(s * a for s, a in zip(score_board, away))

print(home_score, away_score)
