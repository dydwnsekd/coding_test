import sys
import re

atomic_weight = {"C": 12.01, "H": 1.008, "O": 16.00, "N": 14.01}
atomic_regex = re.compile("[CHON]")
num_regex = re.compile("[0-9]")

n = int(sys.stdin.readline())

for i in range(n):
    result = 0
    atomic = sys.stdin.readline().strip()
    atomic_len = len(atomic)
    atomic_count = {"C": 0, "H": 0, "O": 0, "N": 0}

    t = atomic_regex.finditer(atomic)
    index_list = [j.start() for j in t]
    for j in range(len(index_list)-1):
        if index_list[j+1] - index_list[j] == 1:
            atomic_count[atomic[index_list[j]]] += 1
        else:
            atomic_count[atomic[index_list[j]]] += int(atomic[index_list[j]+1:index_list[j+1]])

    for k, v in atomic_count.items():
        result += atomic_weight[k] * atomic_count[k]

    print("{:.3f}".format(result))
