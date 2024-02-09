import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    team_index = -1
    approximate_value = sys.maxsize

    team_value = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(n):
        if abs(2023 - team_value[i]) < approximate_value:
            team_index = i + 1
            approximate_value = abs(2023 - team_value[i])

    print(team_index)
