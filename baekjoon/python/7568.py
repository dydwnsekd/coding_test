import sys

n = int(sys.stdin.readline())
human_list = []
rank_list = [1] * n

for _ in range(n):
    human_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(n-1):
    for j in range(i+1, n):
        if human_list[i][0] > human_list[j][0] and human_list[i][1] > human_list[j][1]:
            rank_list[j] = rank_list[j] + 1
        elif human_list[i][0] < human_list[j][0] and human_list[i][1] < human_list[j][1]:
            rank_list[i] = rank_list[i] + 1

for r in rank_list:
    print(r, end=" ")
