import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num_category = []
    nn = sys.stdin.readline().rstrip()
    for i in nn:
        if i not in num_category:
            num_category.append(i)
    print(len(num_category))
