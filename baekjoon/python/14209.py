import sys

card_score = {"A": 4, "K": 3, "Q": 2, "J":1, "X": 0}
score = 0

cases = int(sys.stdin.readline())

for _ in range(cases):

    card = sys.stdin.readline().strip()

    for c in card:
        score += card_score[c]

print(score)
