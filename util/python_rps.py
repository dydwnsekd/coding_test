import random


def rps(p1, p2):
    RPS_RULES = {
        ("R", "S"): 1, ("R", "P"): 2,
        ("P", "R"): 1, ("P", "S"): 2,
        ("S", "P"): 1, ("S", "R"): 2,
    }

    if p1 == p2:
        return 0
    return RPS_RULES.get((p1, p2), 0)

n = random.randrange(1,4)

if n == 1:
    print("r")
elif n == 2:
    print("p")
else:
    print("s")
