import sys

def quick_partition(sort_list, left, right):
    if len(sort_list) == 1:
        return sort_list
    
    pivot = sort_list[left]

    while (left < right):
        if sort_list[left] < pivot:
            left += 1
            continue

        if sort_list[right] > pivot:
            right -= 1
            continue
        
        sort_list[left], sort_list[right] = sort_list[right], sort_list[left]

    sort_list[0], sort_list[left-1] = sort_list[left-1], sort_list[0]
    pivot_index = left

    return sort_list, pivot_index

def quick(sort_list, left, right):
    if left < right:
        sort_list, pivot_index = quick_partition(sort_list, left, right)

        quick(sort_list, 0, pivot_index-1)
        quick(sort_list, pivot_index+1, right)

    return sort_list

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

sort_list = quick(num_list, 0, len(num_list)-1)

for i in range(n):
    print(sort_list[i])

