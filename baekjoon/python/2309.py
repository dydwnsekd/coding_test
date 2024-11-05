from itertools import combinations

num_list = []

for _ in range(9):
    num_list.append(int(input()))

comb = combinations(num_list, 7)

for c in comb:
    if sum(c) == 100:
        c = sorted(c)

        for i in c:
            print(i)
        break

