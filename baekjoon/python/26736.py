import sys

s = sys.stdin.readline().strip()
a_score = 0
b_score = 0

for i in s:
    if i == "A":
        a_score += 1
    elif i == "B":
        b_score += 1

print(f"{a_score} : {b_score}")
