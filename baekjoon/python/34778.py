import sys

problem_list = set(map(int, sys.stdin.readline().strip().split()))

print(4-len(problem_list))
