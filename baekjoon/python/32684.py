import sys

score = [13, 7, 5, 3, 3, 2]

cocjr0208_score = 0
ekwoo_score = 1.5

cocjr0208_list = list(map(int, sys.stdin.readline().strip().split()))
ekwoo_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(6):
    cocjr0208_score += score[i] * cocjr0208_list[i]
    ekwoo_score += score[i] * ekwoo_list[i]

if cocjr0208_score > ekwoo_score:
    print("cocjr0208")
else:
    print("ekwoo")
