import sys

n, m = map(int, sys.stdin.readline().strip().split())
problem_dict = {}

for _ in range(m):
    p, l = map(int, sys.stdin.readline().strip().split())
    if p not in problem_dict:
        problem_dict[p] = [l]
    elif l not in problem_dict[p]:
        problem_dict[p].append(l)

for problem, language in problem_dict.items():
    if 1 in language and 2 in language:
        print(problem)


