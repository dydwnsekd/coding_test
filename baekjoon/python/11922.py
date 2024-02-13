import sys

result = 0
dominant_score = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
not_dominant_score = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

n, b = sys.stdin.readline().strip().split()
n = int(n)

for _ in range(4*n):
    s = sys.stdin.readline().split()
    if s[1] in dominant_score.keys():
        result += dominant_score[s[0]]
    else:
        result += not_dominant_score[s[0]]

print(result)

