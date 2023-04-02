# TODO
import sys

n, m = map(int, sys.stdin.readline().split())

n_list = []
m_list = []
vote_list = [0] * n
max_index = -1
result = -1

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

for _ in range(m):
    m_list.append(int(sys.stdin.readline()))

for m_score in m_list:
    for i in range(len(n_list)):
        if m_score >= n_list[i]:
            vote_list[i] += 1
            break

for i in range(len(vote_list)):
    if result < vote_list[i]:
        max_index = i+1
        result = vote_list[i]

print(max_index)

