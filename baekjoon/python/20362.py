import sys

answer_list = []
n, s = sys.stdin.readline().split()
n = int(n)

for _ in range(n):
    nickname, answer = sys.stdin.readline().split()
    if nickname == s:
        break
    answer_list.append(answer)

print(answer_list.count(answer))
