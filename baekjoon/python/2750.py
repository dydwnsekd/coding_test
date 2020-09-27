import sys

def bubble(sort_list):
        for i in range(len(sort_list)-1, 0, -1):
            for j in range(0, i):
                if sort_list[j] > sort_list[j+1]:
                    sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
        return sort_list

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list = bubble(num_list)

for i in range(n):
    print(num_list[i])

