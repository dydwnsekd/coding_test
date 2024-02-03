import sys


cases = int(sys.stdin.readline())

for _ in range(cases):
    n, k = map(int, sys.stdin.readline().strip().split())
    my_gene = sys.stdin.readline().strip()

    ancestors_gene = []
    for _ in range(n):
        ancestors_gene.append(list(sys.stdin.readline().strip()))

    pivot_gene = [[row[i] for row in ancestors_gene] for i in range(k)]

