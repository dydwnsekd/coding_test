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
    gold_max = sorted_gold[0][1]
    medal_max = sorted_medal[0][1]

    gold_year = 9999
    medal_year = 9999

    for i in sorted_gold:
        if i[1] == gold_max:
            if gold_year > int(i[0]):
                gold_year = int(i[0])
            else:
                break

    for i in sorted_medal:
        if i[1] == medal_max:
            if medal_year > int(i[0]):
                medal_year = int(i[0])
            else:
                break

    print(gold_year, medal_year)
