import sys

max_score = 0
sequence = 0

for i in range(1, 6):
    score = sum(list(map(int, sys.stdin.readline().split())))
    if max_score < score:
        max_score = score
        sequence = i

print(f"{sequence} {max_score}")
