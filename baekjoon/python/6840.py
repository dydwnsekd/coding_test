import sys

food_weight = []

for _ in range(0, 3):
    food_weight.append(int(sys.stdin.readline()))

food_weight.sort()

print(food_weight[1])
