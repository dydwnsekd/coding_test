import sys

score_list = list(map(int, sys.stdin.readline().strip().split()))
my_score = int(sys.stdin.readline())

rank = score_list.index(my_score) + 1

if 0 <= rank <= 5:
    print("A+")
elif 6 <= rank <= 15:
    print("A0")
elif 16 <= rank <= 30:
    print("B+")
elif 31 <= rank <= 35:
    print("B0")
elif 36 <= rank <= 45:
    print("C+")
elif 46 <= rank <= 48:
    print("C0")
else:
    print("F")

