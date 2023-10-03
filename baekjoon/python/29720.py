import sys

min_value, max_value = 0, 0
n, m, k = list(map(int, sys.stdin.readline().split()))

solve_problem = m * k

if n > solve_problem:
    min_value = n - solve_problem
    max_value = min_value + m - 1
elif n < solve_problem:
    min_value = 0
    max_value = min_value + m - 1

print(min_value, max_value)
