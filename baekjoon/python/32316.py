import sys

n, m = map(int, sys.stdin.readline().strip().split())
problem_dict = {}

for _ in range(m):
    p, l = map(int, sys.stdin.readline().strip().split())
    if p in problem_dict and l not in problem_dict[p]:
        problem_dict[p].append(l)
    else:
        problem_dict[p] = [l]

for problem, language in problem_dict.items():
    if 1 in language and 2 in language:
        print(problem)


