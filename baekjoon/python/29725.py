import sys

white_score = 0
black_score = 0

white_dict = {"K": 0, "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9}
black_dict = {"k": 0, "p": 1, "n": 3, "b": 3, "r": 5, "q": 9}

for _ in range(8):
    line = sys.stdin.readline().strip()

    for s in line:
        if s in white_dict.keys():
            white_score += white_dict[s]
        elif s in black_dict.keys():
            black_score += black_dict[s]

print(white_score - black_score)
