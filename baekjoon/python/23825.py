import sys

s_count, a_count = map(int, sys.stdin.readline().split())

print(min(s_count // 2, a_count // 2))
