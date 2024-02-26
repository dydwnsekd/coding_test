import sys

z = int(sys.stdin.readline())

for _ in range(z):
    count_dict = {"N": 0, "S": 0, "W": 0, "E": 0}
    result = 0
    n = int(sys.stdin.readline())

    direction_list = list(sys.stdin.readline().strip())

    for direction in direction_list:
        count_dict[direction] += 1

    result += abs(count_dict["N"] - count_dict["S"]) + abs(count_dict["W"] - count_dict["E"])
    print(result)

