import sys

def rps(p1, p2):
    RPS_RULES = {
        ("R", "S"): 1, ("R", "P"): 2,
        ("P", "R"): 1, ("P", "S"): 2,
        ("S", "P"): 1, ("S", "R"): 2,
    }

    if p1 == p2:
        return 0
    return RPS_RULES.get((p1, p2), 0)


n = int(sys.stdin.readline())

p1 = sys.stdin.readline().strip()
p2 = sys.stdin.readline().strip()

win_count = 0
lose_count = 0

for i in range(n):
    if rps(p1[i], p2[i]) == 1:
        win_count += 1
    elif rps(p1[i], p2[i]) == 2:
        lose_count += 1

if win_count > lose_count:
    print("victory")
else:
    print("defeat")

