from collections import defaultdict
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    str_dict = defaultdict(int)
    line = sys.stdin.readline().replace(" ", "").strip()

    for s in line:
        str_dict[s] += 1

    count_list = sorted(str_dict.items(), key=lambda count_value: count_value[1], reverse=True)
    alpha = [x[0] for x in count_list]
    alpha_count = [x[1] for x in count_list]

    if alpha_count.count(alpha_count[0]) == 1:
        print(alpha[0])
    else:
        print("?")
