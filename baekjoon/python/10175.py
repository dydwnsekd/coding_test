import sys
from collections import Counter

cases = int(sys.stdin.readline())
weight_dict = {"B": 2, "C": 1, "M": 4, "W": 3}

for _ in range(cases):
    result_dict = {}
    region, species = sys.stdin.readline().split()
    species = list(species)

    count_species = Counter(species)
    for k, v in count_species.items():
        result_dict[k] = v * weight_dict[k]

    print(result_dict)
