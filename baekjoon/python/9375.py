import sys
from collections import defaultdict

category_dict = defaultdict(int)

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    answer = 1
    category_dict = defaultdict(int)

    for _ in range(m):
        name, clothes_type = sys.stdin.readline().split()
        category_dict[clothes_type] += 1

    for k, v in category_dict.items():
        answer *= (v+1)

    print(answer-1)

