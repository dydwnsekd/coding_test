import sys

n, m = map(int, sys.stdin.readline().split())

n_list = list(map(int, sys.stdin.readline().split()))
m_list = list(map(int, sys.stdin.readline().split()))

print(max(n_list) + max(m_list))
