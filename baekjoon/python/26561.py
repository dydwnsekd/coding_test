import sys

birth_cycle = 4
dead_cycle = 7

cases = int(sys.stdin.readline())

for _ in range(cases):
    people, times = list(map(int, sys.stdin.readline().split()))

    people += times // birth_cycle
    people -= times // dead_cycle

    print(people)

