import sys

def rps(p1, p2):
    if p1 == "R" and p2 == "R":
        return 0
    elif p1 == "R" and p2 == "P":
        return 2
    elif p1 == "R" and p2 == "S":
        return 1
    elif p1 == "P" and p2 == "R":
        return 1
    elif p1 == "P" and p2 == "P":
        return 0
    elif p1 == "P" and p2 == "S":
        return 2
    elif p1 == "S" and p2 == "R":
        return 2
    elif p1 == "S" and p2 == "P":
        return 1
    elif p1 == "S" and p2 == "S":
        return 0


n = int(sys.stdin.readline())

p1 = sys.stdin.readline()
p2 = sys.stdin.readline()

win_count = 0

for i in range(n):
    if rps(p1, p2) == 1:
        win_count += 1

if win_count > n // 2:
    print("victory")
else:
    print("defeat")

