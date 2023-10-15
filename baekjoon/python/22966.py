import sys

level = 5
easy_name = ""
cases = int(sys.stdin.readline())

for _ in range(cases):
    name, problem_level = sys.stdin.readline().strip().split()
    problem_level = int(problem_level)

    if level > problem_level:
        easy_name = name
        level = problem_level

print(easy_name)
