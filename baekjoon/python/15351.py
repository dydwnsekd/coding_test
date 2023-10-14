import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    score = 0
    string = sys.stdin.readline().strip().replace(" ", "")
    for s in string:
        score += ord(s) - 64

    if score == 100:
        print("PERFECT LIFE")
    else:
        print(score)

