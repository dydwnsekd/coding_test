import sys

weight = [2, 7, 6, 5, 4, 3, 2]
mapping_dict = {0: "J", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "Z"}
total = 0

n = sys.stdin.readline().strip()

for i in range(len(weight)):
    total += int(n[1]) * weight[i]

print(mapping_dict[total % 11])
