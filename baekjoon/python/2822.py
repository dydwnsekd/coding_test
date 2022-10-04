import sys

score_list = []
index_list = []

for _ in range(8):
    score_list.append(int(sys.stdin.readline()))

sorted_list = sorted(score_list)

print(sum(sorted_list[3:]))

for i in sorted_list[3:]:
    index_list.append(score_list.index(i) + 1)

index_list.sort()

for i in index_list:
    print(i, end=" ")
