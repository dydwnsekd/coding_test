import sys
from collections import defaultdict

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    gold_dict = defaultdict(int)
    medal_dict = defaultdict(int)

    for _ in range(n):
        year, event, medal = sys.stdin.readline().strip().split()
        if medal == "Gold":
            gold_dict[year] += 1

        medal_dict[year] += 1

    print(gold_dict)
    print(medal_dict)
