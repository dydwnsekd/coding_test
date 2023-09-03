# https://developer-next-to-you.tistory.com/m/246
"""
import sys

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
"""

import sys
from collections import Counter

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    gold_count = Counter()
    medal_count = Counter()

    for _ in range(n):
        year, event, medal = sys.stdin.readline().strip().split()
        if medal == "Gold":
            gold_count[year] += 1
        medal_count[year] += 1

    max_gold = max(gold_count.values())
    max_medal = max(medal_count.values())

    gold_years = [year for year, count in gold_count.items() if count == max_gold]
    medal_years = [year for year, count in medal_count.items() if count == max_medal]

    print(min(gold_years), min(medal_years))
