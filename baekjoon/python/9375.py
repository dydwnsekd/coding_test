import sys
from collections import defaultdict

category_dict = defaultdict(int)

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    category_dict = defaultdict(int)

    for _ in range(m):
        name, clothes_type = sys.stdin.readline().split()
        category_dict[clothes_type] += 1

    print(category_dict)



