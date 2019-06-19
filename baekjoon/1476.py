import sys

# E 15, S 28, M 19
E, S, M = map(int, sys.stdin.readline().split(" "))

candidate_list = list()

for i in range(S, 7981, 28):
    candidate_list.append(i)

temp_list = list()
for i in range(M, 7981, 19):
    if i in candidate_list:
        temp_list.append(i)
candidate_list = temp_list.copy()

temp_list = list()
for i in range(E, 7981, 15):
    if i in candidate_list:
        temp_list.append(i)
candidate_list = temp_list.copy()

print (candidate_list[0])
