import sys

value_list = [350.34, 230.90, 190.55, 125.30, 180.90]

n = int(sys.stdin.readline())

for _ in range(n):
    value = 0
    parts = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(len(parts)):
         value += value_list[i] * parts[i]

    print(f"${value:.2f}")

