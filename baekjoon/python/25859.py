from collections import Counter

s = input().strip()

counter = Counter(s)

sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for char, cnt in sorted_items:
    print(char * cnt, end="")
