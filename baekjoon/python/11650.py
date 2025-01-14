import sys

n = int(sys.stdin.readline())
coordinates_list = []
for _ in range(n):
    coordinates_list.append(list(map(int, sys.stdin.readline().split())))

coordinates_list = sorted(coordinates_list, key=lambda coordinates_list: [coordinates_list[0], coordinates_list[1]])

for x, y in coordinates_list:
    print(x, y)
