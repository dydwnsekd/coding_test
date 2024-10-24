import sys

n = int(sys.stdin.readline())

for i in range(n):
    num_list = sorted(list(map(int, sys.stdin.readline().split())))

    print(f"Scenario {i}:")
    if num_list[0] ** 2 + num_list[1] ** 2 == num_list[2] ** 2:
        print("yes")
    else:
        print("no")

