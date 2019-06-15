import sys

problem_count = int(sys.stdin.readline())

for _ in range(problem_count):
    a, b = list(map(int, sys.stdin.readline().split(" ")))

    print (a+b)
