import sys

def insertion(sort_list):
    for i in range(1, len(sort_list)):
        idx = i

        for j in range(i-1, -1, -1):
            if sort_list[idx] < sort_list[j]:
                sort_list[idx], sort_list[j] = sort_list[j], sort_list[idx]
                idx = j
            else:
                break
    return sort_list

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list = insertion(num_list)

for i in range(n):
    print(num_list[i])

