# https://developer-next-to-you.tistory.com/m/246

import sys
from collections import defaultdict
"""
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    gold_dict = defaultdict(int)
    medal_dict = defaultdict(int)
    gold_year = 9999
    medal_year = 9999

    for _ in range(n):
        year, event, medal = sys.stdin.readline().strip().split()
        if medal == "Gold":
            gold_dict[year] += 1

        medal_dict[year] += 1

    sorted_gold = sorted(gold_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_medal = sorted(medal_dict.items(), key=lambda item: item[1], reverse=True)
    gold_max = sorted_gold[0][1]
    medal_max = sorted_medal[0][1]

    for i in sorted_gold:
        if i[1] >= gold_max:
            if gold_year > int(i[0]):
                gold_year = int(i[0])
            else:
                break

    for i in sorted_medal:
        if i[1] >= medal_max:
            if medal_year > int(i[0]):
                medal_year = int(i[0])
            else:
                break

    print(gold_year, medal_year)
"""

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    gold_list = []
    medal_list = []

    for _ in range(n):
        year, event, medal = sys.stdin.readline().strip().split()
        if medal == "Gold":
            gold_list.append(year)

        medal_list.append(year)

    set_gold = set(gold_list)
    set_medal = set(medal_list)

    max_gold = 0
    gold_year = 9999
    max_medal = 0
    medal_year = 9999

    for g in set_gold:
        if gold_list.count(g) > max_gold:
            gold_year = g
            max_gold = gold_list.count(g)
        elif gold_list.count(g) == max_gold:
            if gold_year > g:
                gold_year = g

    for m in set_medal:
        if medal_list.count(m) > max_medal:
            medal_year = m
            max_medal = medal_list.count(m)
        elif medal_list.count(m) == max_medal:
            if medal_year > m:
                medal_year = m

    print(gold_year, medal_year)

