import sys
from collections import Counter

cases = int(sys.stdin.readline())
weight_dict = {"B": 2, "C": 1, "M": 4, "W": 3}
animal_dict = {"B": "Bobcat", "C": "Coyote", "M": "Mountain Lion", "W": "Wolf"}

for _ in range(cases):
    result_dict = {}
    region, species = sys.stdin.readline().split()
    species = list(species)

    count_species = Counter(species)
    for k, v in count_species.items():
        result_dict[k] = v * weight_dict[k]

    sorted_list = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    if sorted_list[0][1] == sorted_list[1][1]:
        print(f"{region}: There is no dominant species")
    else:
        print(f"{region}: The {animal_dict[sorted_list[0][0]]} is the dominant species")
