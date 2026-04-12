"""
import sys

n, m = map(int, sys.stdin.readline().strip().split())
problem_dict = {}

for _ in range(m):
    p, l = map(int, sys.stdin.readline().strip().split())
    if p not in problem_dict:
        problem_dict[p] = [l]
    elif l not in problem_dict[p]:
        problem_dict[p].append(l)

problem_result = []

for problem, language in problem_dict.items():
    if 1 in language and 2 in language:
        problem_result.append(problem)

print(*sorted(problem_result))
"""

import sys

n, m = map(int, sys.stdin.readline().split())
problem_dict = {}

for _ in range(m):
    p, l = map(int, sys.stdin.readline().split())
    problem_dict.setdefault(p, set()).add(l)

result = [p for p, langs in problem_dict.items() if {1, 2}.issubset(langs)]

print(*sorted(result))

