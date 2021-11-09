import sys

human_count = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]

for i in range(1, 15):
    temp_list = []
    for j in range(0, 14):
        temp_list.append(sum(human_count[0][:j+1]))
    human_count.insert(0, temp_list)

human_count.reverse()

T = int(sys.stdin.readline())
for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(human_count[k][n-1])