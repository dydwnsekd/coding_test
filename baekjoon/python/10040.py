"""
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
"""

import sys

n, m = map(int, sys.stdin.readline().split())
costs = [int(sys.stdin.readline()) for _ in range(n)]
votes = [0] * n

for i in range(m):
    song_cost = int(sys.stdin.readline())
    min_cost, min_idx = float('inf'), -1
    for j in range(n):
        if costs[j] <= song_cost and costs[j] < min_cost:
            min_cost, min_idx = costs[j], j
    if min_idx >= 0:
        votes[min_idx] += 1

max_idx = 0
for i in range(1, n):
    if votes[i] > votes[max_idx]:
        max_idx = i
print(max_idx+1)
