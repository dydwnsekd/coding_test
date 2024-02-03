import sys

cases = int(sys.stdin.readline())

for i in range(cases):
    n, k = map(int, sys.stdin.readline().strip().split())
    my_gene = sys.stdin.readline().strip()

    ancestors_gene = []
    for _ in range(n):
        ancestors_gene.append(list(sys.stdin.readline().strip()))

    pivot_gene = [[row[i] for row in ancestors_gene] for i in range(k)]

    result = 0
    for j in range(k):
        if my_gene[j] not in pivot_gene[j]:
            result += 1

    print(f"Data Set {i+1}:")
    print(f"{result}/{k}\n")
