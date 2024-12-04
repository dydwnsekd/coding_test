import sys

cases = int(sys.stdin.readline())

for _ in range(cases):
    result = 0
    turtle_count = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(len(turtle_count)):
        if turtle_count[i+1] == 0:
            break
        elif turtle_count[i] * 2 < turtle_count[i+1]:
            result += turtle_count[i+1] - (turtle_count[i] * 2)

    print(result)
