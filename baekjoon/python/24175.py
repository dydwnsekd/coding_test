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

    sorted_gold = sorted(gold_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_medal = sorted(medal_dict.items(), key=lambda item: item[1], reverse=True)

    print(sorted_gold[0][0], sorted_medal[0][0])
